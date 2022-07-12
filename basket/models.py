import datetime

from django.db import models
from auth_.models import MyUser
from api.models import Product
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u"Пользователь")
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u"Товар")
    quantity = models.IntegerField(null=False, verbose_name=u"Количество покупок")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'Добавить время')
    updated_at = models.DateTimeField(auto_now=True, verbose_name=u'Обновленное время')

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.user,
                                               self.item,
                                               self.quantity,
                                               self.created_at,
                                               self.updated_at)


class DeliveryCost(models.Model):
    status = models.CharField(max_length=7, choices=(('Active', 'active'), ('Passive', 'passive')), default='passive', null=False)
    cost_per_delivery = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    cost_per_product = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    fixed_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} ".format(self.status,
                                                     self.cost_per_delivery,
                                                     self.cost_per_product,
                                                     self.fixed_cost,
                                                     self.create_at,
                                                     self.update_at)