# Generated by Django 3.1 on 2020-08-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(default='destination_4.jpg', upload_to='pics')),
                ('desc', models.TextField(default='Defualt Value')),
                ('price', models.IntegerField(default=0)),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DirectoryMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(blank=True, max_length=250)),
                ('Bio', models.TextField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='memberdirectory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('img', models.ImageField(default='', upload_to='pics')),
                ('desc', models.TextField(default='Defualt Value')),
                ('size', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('coupon', models.CharField(blank=True, max_length=100, null=True)),
                ('is_superuser', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]