# Generated by Django 4.2.6 on 2023-10-15 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine_app', '0002_rename_produto_cadastro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cadastro',
            old_name='desc_produto',
            new_name='descrição',
        ),
    ]
