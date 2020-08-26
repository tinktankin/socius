# Generated by Django 3.0.8 on 2020-08-22 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socius', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memberdirectory',
            old_name='desc',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='memberdirectory',
            old_name='name',
            new_name='DirectoryName',
        ),
        migrations.RenameField(
            model_name='memberdirectory',
            old_name='size',
            new_name='MemberLimit',
        ),
        migrations.AddField(
            model_name='memberdirectory',
            name='img',
            field=models.ImageField(default='', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='memberdirectory',
            name='user',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DirectoryMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(blank=True, max_length=250)),
                ('Bio', models.TextField(blank=True, max_length=250, null=True)),
                ('Directory', models.ManyToManyField(to='socius.memberdirectory')),
                ('memberdirectory_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memberdirectory_id', to='socius.memberdirectory')),
            ],
        ),
    ]