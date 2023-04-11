from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Пункт"
        verbose_name_plural = "Пункты"
    def __str__(self):
        return self.name


class Purchase(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_purchase = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Покупок"
        verbose_name_plural = "Покупки"

    def __str__(self):
        return f'{self.name}{self.age}{self.item}'
