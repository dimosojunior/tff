# Generated by Django 3.2.5 on 2022-03-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0013_auto_20220324_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratiba',
            name='post_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='results',
            name='post_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
