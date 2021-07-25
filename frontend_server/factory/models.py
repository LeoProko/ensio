from django.db import models

class Password(models.Model):
    service = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.service)

class Employee(models.Model):
    STATUS = (
        ('Works', 'Works'),
        ('Dismissed', 'Dismissed'),
        ('On holiday', 'On holiday'),
    )

    POSITION = (
        ('Manager', 'Manager'),
        ('Deliveryman', 'Deliveryman'),
        ('CEO', 'CEO'),
        ('CTO', 'CTO'),
        ('Founder', 'Founder'),
    )

    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=50, choices=POSITION)
    status = models.CharField(max_length=50, choices=STATUS)
    phone_number = models.CharField(max_length=20)
    telegram = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100)
    start_date = models.DateField()
    birthday = models.DateField()

    def __str__(self) -> str:
        return self.first_name + ' ' + self.surname + ': ' + self.position

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
    weight = models.CharField(max_length=10, null=True)
    materials = models.ManyToManyField(Material)
    sizes = models.ManyToManyField(Size)
    tags = models.ManyToManyField(Tag)
    stock_balance = models.FloatField(null=True)
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

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.surname

class CustomerOrder(models.Model):
    STATUS = (
        ('Получен', 'Получен'),
        ('В работе', 'В работе'),
        ('Готовится к доставке', 'Готовится к доставке'),
        ('В пути', 'В пути'),
        ('Доставлен', 'Доставлен'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self) -> str:
        return str(self.customer.first_name) + ' ' +\
            str(self.customer.surname) + ' ' + str(self.status)

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
    contacts = models.CharField(max_length=50, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    size = models.CharField(max_length=10, null=True)
    comment = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS, null=True, default='Получен')
    date_created = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return str(self.customer_name)

class Document(models.Model):
    title = models.CharField(max_length=200, null=True)
    owner = models.CharField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    markdown_data = models.TextField(null=True)
    html_data = models.TextField(null=True)

    def __str__(self) -> str:
        return str(self.title)

class Task(models.Model):
    done = models.BooleanField(default=False)
    task = models.TextField(null=True)
    deadline = models.DateField()
    chief = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='chief')
    executors = models.ManyToManyField(Employee, related_name='executors')

    def __str__(self) -> str:
        return str(self.task)

