from rest_framework.exceptions import ParseError, NotFound

from app.models import SalePoint, Visiting



class Accessor:

    @staticmethod
    def get_phone(request):
        return request.META.get('HTTP_PHONE')

    @staticmethod
    def get_sale_point(data):
        return SalePoint.objects.filter(pk=data.get('sale_point'))

    @staticmethod
    def get_worker_id(sale_point) -> int:
        try:
            return sale_point.values('worker_id')[0].get('worker_id')
        except IndexError:
            raise NotFound(detail='Not found sale_point')

    @staticmethod
    def create_visit(data):
        return Visiting.objects.create(sale_point_id=data['sale_point'],
                                       latitude=data['latitude'],
                                       longitude=data['longitude'])
