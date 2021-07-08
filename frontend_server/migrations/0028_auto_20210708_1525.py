# Generated by Django 2.2.12 on 2021-07-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend_server', '0027_auto_20210708_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='status',
            field=models.CharField(choices=[('Received', 'Получен'), ('In work', 'В работе'), ('Ready to deliver', 'Готовится к доставке'), ('On the way', 'В пути'), ('Delivered', 'Доставлен')], max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Received', 'Получен'), ('In work', 'В работе'), ('Ready to deliver', 'Готовится к доставке'), ('On the way', 'В пути'), ('Delivered', 'Доставлен')], default='Получен', max_length=50, null=True),
        ),
    ]
