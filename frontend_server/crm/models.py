from django.db import models

from shop.models import Item

class Order(models.Model):
    STATUS = (
        ('Получен', 'Получен'),
        ('В работе', 'В работе'),
        ('Готовится к доставке', 'Готовится к доставке'),
        ('В пути', 'В пути'),
        ('Доставлен', 'Доставлен'),
    )

    customer_name = models.CharField(max_length=50, null=True)
    connection_type = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    size = models.CharField(max_length=10, null=True)
    comment = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS, null=True, default='Получен')
    date_created = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return str(self.customer_name)
