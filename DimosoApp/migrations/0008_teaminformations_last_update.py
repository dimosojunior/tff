# Generated by Django 3.2.5 on 2022-03-19 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0007_teams_u'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaminformations',
            name='last_update',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]