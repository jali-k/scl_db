# Generated by Django 4.2 on 2023-05-01 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sclmain', '0003_schooldetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='schooldetails',
            name='latestDescription2',
            field=models.CharField(max_length=500, null=True),
        ),
    ]