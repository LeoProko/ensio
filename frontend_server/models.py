from django.db import models

class Password(models.Model):
    service = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.service

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

    def __str__(self):
        return self.first_name + ' ' + self.surname + ': ' + self.position

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    price = models.FloatField()
    stock_balance = models.FloatField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.surname

class Order(models.Model):
    STATUS = (
        ('Received', 'Received'),
        ('In work', 'In work'),
        ('Ready to deliver', 'Ready to deliver'),
        ('On the way', 'On the way'),
        ('Delivered', 'Deliverd'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
        return self.customer.first_name + ' ' + self.customer.surname + ' ' + self.status

