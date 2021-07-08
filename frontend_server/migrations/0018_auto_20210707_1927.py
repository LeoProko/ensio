# Generated by Django 2.2.12 on 2021-07-07 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend_server', '0017_auto_20210707_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Received', 'Received'), ('In work', 'In work'), ('Ready to deliver', 'Ready to deliver'), ('On the way', 'On the way'), ('Delivered', 'Deliverd')], default='Received', max_length=50, null=True),
        ),
    ]
