# Generated by Django 3.0.3 on 2020-09-03 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='case_pic',
            field=models.ImageField(blank=True, upload_to='case_pic'),
        ),
    ]
