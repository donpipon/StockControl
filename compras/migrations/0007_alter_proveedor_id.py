# Generated by Django 5.0.3 on 2024-03-29 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0006_alter_producto_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
