# Generated by Django 2.2.12 on 2021-05-29 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend_server', '0002_auto_20210529_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Deliveryman', 'Deliveryman'), ('CEO', 'CEO'), ('CTO', 'CTO'), ('Founder', 'Founder')], max_length=50),
        ),
    ]
