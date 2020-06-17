from django.db import models
from django.contrib.auth.models import User



class Topping(models.Model):
    toppingsType = models.CharField(max_length=100, null=True)
    forPizza = models.BooleanField(default=True)
    forSub = models.BooleanField(default=False)

    def __str__(self):
         return f"{self.toppingsType}"

class MenuItem(models.Model):
    itemName = models.CharField(max_length=100)

    def __str__(self):
        return self.itemName

class ItemType(models.Model):
    itemId = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    itemType = models.CharField(max_length=100)

    def __str__(self):
        return self.itemType

class Price(models.Model):
    itemTypeId = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    size = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f"{self.itemTypeId} - {self.size}"

class Cart(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    itemType = models.ForeignKey(ItemType, on_delete=models.CASCADE, default=1)
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topping1 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name="cart_topping1", null=True)
    topping2 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name="cart_topping2", null=True)
    topping3 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name="cart_topping3", null=True)
    ordered = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.item} - {self.itemType} - {self.user}"

# class UserOrder(models.Model):
#     userOrder = models.ForeignKey(Cart, on_delete=models.CASCADE, default=None)
#     completed = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.userOrder}"