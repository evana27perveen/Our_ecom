from django.db import models

# Create your models here.
from App_login.models import CustomUser
from App_store.models import ProductModel


class CartModel(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='buyer')
    order = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='each_order')
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=200)
    total_price = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)

    def get_price(self):
        total_price = self.quantity * round(self.order.selling_price)
        return format(total_price, "0.2f")


class OrderModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='order_user')
    my_cart = models.ForeignKey(CartModel, on_delete=models.CASCADE, related_name='carts')
    created = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)
    sub_total = models.PositiveIntegerField(default=0)
