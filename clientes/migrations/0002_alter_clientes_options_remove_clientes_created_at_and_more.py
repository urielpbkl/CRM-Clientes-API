# Generated by Django 4.0.5 on 2022-06-08 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientes',
            options={'ordering': ['id'], 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='updated_at',
        ),
    ]