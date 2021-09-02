# Generated by Django 2.2.12 on 2021-08-31 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0002_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50, null=True)),
                ('connection_type', models.CharField(max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=50, null=True)),
                ('size', models.CharField(max_length=10, null=True)),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(choices=[('Получен', 'Получен'), ('В работе', 'В работе'), ('Готовится к доставке', 'Готовится к доставке'), ('В пути', 'В пути'), ('Доставлен', 'Доставлен')], default='Получен', max_length=50, null=True)),
                ('date_created', models.DateTimeField(null=True)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Item')),
            ],
        ),
    ]