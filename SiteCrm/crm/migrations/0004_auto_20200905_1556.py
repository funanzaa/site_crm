# Generated by Django 3.0.3 on 2020-09-05 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20200905_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='date_entered',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='case',
            name='update_at',
            field=models.DateTimeField(),
        ),
    ]
