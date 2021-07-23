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
    item_image = models.ImageField(upload_to='stock_photo/', null=True)

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.customer.first_name + ' ' + self.customer.surname + ' ' + self.status

class Order(models.Model):
    STATUS = (
        ('Получен', 'Получен'),
        ('В работе', 'В работе'),
        ('Готовится к доставке', 'Готовится к доставке'),
        ('В пути', 'В пути'),
        ('Доставлен', 'Доставлен'),
    )

    CONNECTION = (
        ('Phone', 'Телефон'),
        ('Telegram', 'Телеграм'),
        ('Whats App', 'Вотс ап'),
        ('Instagram', 'Инстаграм'),
    )

    SIZE = (
        ('15', '15'),
        ('15.5', '15.5'),
        ('16', '16'),
        ('16.5', '16.5'),
        ('17', '17'),
        ('17.5', '17.5'),
        ('18', '18'),
        ('18.5', '18.5'),
        ('19', '19'),
        ('19.5', '19.5'),
        ('20', '20'),
        ('20.5', '20.5'),
        ('21', '21'),
    )

    customer_name = models.CharField(max_length=50, null=True)
    connection_type = models.CharField(max_length=50, choices=CONNECTION, null=True)
    contacts = models.CharField(max_length=50, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    size = models.CharField(max_length=50, null=True, choices=SIZE)
    comment = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS, null=True, default='Получен')
    date_created = models.DateTimeField(null=True)

    def __str__(self):
        return self.customer_name

class Document(models.Model):
    title = models.CharField(max_length=200, null=True)
    owner = models.CharField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    markdown_data = models.TextField(null=True)
    html_data = models.TextField(null=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    done = models.BooleanField(default=False)
    task = models.TextField(null=True)
    deadline = models.DateField()
    chief = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='chief')
    executors = models.ManyToManyField(Employee, related_name='executors')

    def __str__(self):
        return self.task

