# Generated by Django 3.1 on 2020-09-07 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_document_fileextension'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]