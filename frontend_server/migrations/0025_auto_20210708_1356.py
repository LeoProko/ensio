# Generated by Django 2.2.12 on 2021-07-08 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend_server', '0024_auto_20210708_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]