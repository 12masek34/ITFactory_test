from django.contrib import admin

from .models import Worker, SalePoint, Visiting


class SalePointAdmin(admin.ModelAdmin):
    list_display = ('name', 'worker')
    search_fields = ('name',)


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name',)


class VisitingAdmin(admin.ModelAdmin):
    readonly_fields = ('sale_point', 'visit_date', 'get_worker')
    list_display = ('sale_point', 'visit_date', 'get_worker')
    search_fields = ('sale_point__worker__name', 'sale_point__name')

    def get_worker(self, obj):
        return obj.sale_point.worker


admin.site.register(Worker, WorkerAdmin)
admin.site.register(SalePoint, SalePointAdmin)
admin.site.register(Visiting, VisitingAdmin)
