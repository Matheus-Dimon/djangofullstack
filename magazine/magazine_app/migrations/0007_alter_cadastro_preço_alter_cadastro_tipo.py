# Generated by Django 4.2.6 on 2023-10-22 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine_app', '0006_alter_cadastro_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='preço',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='tipo',
            field=models.TextField(max_length=255),
        ),
    ]
