# Generated by Django 4.2.4 on 2023-08-08 19:14

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('role', models.CharField(choices=[('rector', 'Ректор'), ('secretary', 'Секретарша')], max_length=256, verbose_name='Роль')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Моб. телефон')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Статус персонала')),
            ],
            options={
                'verbose_name': 'Учетная запись',
                'verbose_name_plural': 'Учетные записи',
            },
        ),
    ]