# Generated by Django 2.2.12 on 2021-07-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend_server', '0026_auto_20210708_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Received', 'Получен'), ('In work', 'В работе'), ('Ready to deliver', 'Готовится к доставке'), ('On the way', 'В пути'), ('Delivered', 'Доставлен')], default='Received', max_length=50, null=True),
        ),
    ]