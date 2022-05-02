from django.db import models


class Worker(models.Model):
    name = models.CharField('Работник', max_length=255)
    phone = models.CharField('Телефон', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Рабтники'


class SalePoint(models.Model):
    name = models.CharField('Название', max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'


class Visiting(models.Model):
    visit_date = models.DateTimeField('Дата визита', auto_now=True)
    sale_point = models.ForeignKey(SalePoint, on_delete=models.CASCADE)
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'
