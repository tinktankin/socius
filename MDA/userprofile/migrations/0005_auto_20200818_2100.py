# Generated by Django 3.0.8 on 2020-08-18 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0004_contactinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='countryCode',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='emails',
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
