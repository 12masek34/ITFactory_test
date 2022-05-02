from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import SalePoint, Worker, Visiting
from .serializers import SalePointSerializer, RequestVisitSerializer, ResponseSerializer
from .service import Accessor


class SalePointList(ModelViewSet, Accessor):

    def get_serializer_class(self):
        if self.action == 'list':
            return SalePointSerializer
        if self.action == 'create':
            return RequestVisitSerializer

    def get_queryset(self):
        phone = self.get_phone(self.request)
        if phone is None:
            raise NotFound(detail='No phone number in the header')
        try:
            worker = Worker.objects.get(phone=phone)
        except Worker.DoesNotExist:
            raise ValidationError(detail='This phone doesnt have a match sale_point')
        sale_points = SalePoint.objects.filter(worker=worker.id)
        return sale_points

    def list(self, request, *args, **kwargs):
        sale_points = self.get_queryset()
        serializer = SalePointSerializer(sale_points, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = RequestVisitSerializer(request.data)
        sale_point = self.get_sale_point(serializer.data)
        worker_id = self.get_worker_id(sale_point)
        phone = self.get_phone(request)
        try:
            worker = Worker.objects.get(phone=phone)
        except Worker.DoesNotExist:
            raise NotFound(detail='No phone number in the header')

        if worker_id == worker.id:
            visit = self.create_visit(serializer.data)
            serializer = ResponseSerializer(visit)
            return Response(serializer.data)
        else:
            raise ValidationError(detail='The sale_point is not associated with your phone number')
