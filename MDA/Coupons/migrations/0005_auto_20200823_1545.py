# Generated by Django 3.1 on 2020-08-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coupons', '0004_auto_20200821_1558'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CouponAdmin',
        ),
        migrations.DeleteModel(
            name='CouponSU',
        ),
        migrations.DeleteModel(
            name='ReferralforMember',
        ),
        migrations.AddField(
            model_name='coupon_su',
            name='Directory',
            field=models.CharField(choices=[('a', 'a'), ('b', 'b')], max_length=100, null=True),
        ),
    ]