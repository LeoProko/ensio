from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.name)

class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.name)

class Size(models.Model):
    size = models.CharField(max_length=5)

    def __str__(self) -> str:
        return str(self.size)

def main_photo_path(instance, filename) -> str:
    return f'item_photos/{instance.name_id}/{filename}'

class Item(models.Model):
    name_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    weight = models.CharField(max_length=10, null=True, blank=True)
    materials = models.ManyToManyField(Material)
    sizes = models.ManyToManyField(Size)
    tags = models.ManyToManyField(Tag)
    stock_balance = models.FloatField(null=True)
    # TODO
    # autoprocess of main photo after uploading:
    # - convert to 3x4
    # - add white fog to the top and bottom
    main_photo = models.ImageField(upload_to=main_photo_path, null=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return str(self.name) + ': ' + str(self.name_id)

def get_image_path(instance, filename) -> str:
    return f'item_photos/{instance.item.name_id}/{filename}'

class ItemImage(models.Model):
    # all images have to be 4x3
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to=get_image_path, null=True)

    def __str__(self):
        return 'image of ' + self.item.name

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
