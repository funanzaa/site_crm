# Generated by Django 3.0.3 on 2020-09-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_auto_20200905_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
