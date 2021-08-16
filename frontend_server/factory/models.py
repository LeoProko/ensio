from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import Group

class UserManager(BaseUserManager):
    def create_user(self, email, phone_number,
                    public_name, password,
                    **other_fileds):
        if not email:
            raise ValueError('Incorrect email')

        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number,
                          public_name=public_name, **other_fileds)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, phone_number,
                    public_name, password,
                    **other_fileds):
        other_fileds.setdefault('is_staff', True)
        other_fileds.setdefault('is_superuser', True)
        other_fileds.setdefault('is_active', True)

        return self.create_user(email, phone_number,
                    public_name, password, **other_fileds)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, null=True, unique=True)
    email = models.EmailField(max_length=100, null=True, unique=True)
    phone_number = models.CharField(max_length=20, null=True)
    public_name = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    second_name = models.CharField(max_length=20, null=True, blank=True)
    father_name = models.CharField(max_length=20, blank=True, null=True)
    telegram = models.CharField(max_length=50, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    def __str__(self) -> str:
        return str(self.username) + ' : ' + str(self.first_name) + ' ' + str(self.second_name)

class Password(models.Model):
    service = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.service)

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

class Document(models.Model):
    title = models.CharField(max_length=200, null=True)
    owner = models.CharField(max_length=50, null=True)
    authors = models.ManyToManyField(User)
    groups = models.ManyToManyField(Group)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    markdown_data = models.TextField(null=True)
    html_data = models.TextField(null=True)
    is_link_public = models.BooleanField(default=False)
    is_indexed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.title)

class Task(models.Model):
    done = models.BooleanField(default=False)
    task = models.TextField(null=True)
    deadline = models.DateField()
    chief = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chief')
    executors = models.ManyToManyField(User, related_name='executors')

    def __str__(self) -> str:
        return str(self.task)

