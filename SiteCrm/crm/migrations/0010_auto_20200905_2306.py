# Generated by Django 3.0.3 on 2020-09-05 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20200905_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_pic',
            field=models.ImageField(blank=True, upload_to='case/img/'),
        ),
    ]
