# Generated by Django 3.1.7 on 2021-03-31 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_cliente', models.CharField(max_length=50)),
                ('Dirección_electronico', models.EmailField(max_length=40)),
                ('contra', models.CharField(max_length=60)),
                ('Telefono', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Dirección', models.EmailField(max_length=40)),
                ('Telefono', models.CharField(max_length=60)),
                ('Nombre_producto', models.CharField(max_length=60)),
                ('Precio', models.CharField(max_length=60)),
            ],
        ),
    ]
