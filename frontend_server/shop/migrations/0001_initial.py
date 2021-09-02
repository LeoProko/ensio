# Generated by Django 2.2.12 on 2021-08-19 16:10

from django.db import migrations, models
import django.db.models.deletion
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_id', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('price', models.FloatField(null=True)),
                ('weight', models.CharField(blank=True, max_length=10, null=True)),
                ('stock_balance', models.FloatField(null=True)),
                ('main_photo', models.ImageField(null=True, upload_to=shop.models.main_photo_path)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
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
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=shop.models.get_image_path)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='materials',
            field=models.ManyToManyField(to='shop.Material'),
        ),
        migrations.AddField(
            model_name='item',
            name='sizes',
            field=models.ManyToManyField(to='shop.Size'),
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(to='shop.Tag'),
        ),
    ]