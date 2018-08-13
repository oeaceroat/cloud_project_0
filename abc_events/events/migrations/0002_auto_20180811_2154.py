# Generated by Django 2.1 on 2018-08-11 21:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name_plural': 'Usuarios en la plataforma'},
        ),
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(help_text='Required. Letters, digits and @/./+/-/_ only.', max_length=254, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid email address.', 'invalid')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this site.', verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, null=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], verbose_name='username'),
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='auth_user',
        ),
    ]