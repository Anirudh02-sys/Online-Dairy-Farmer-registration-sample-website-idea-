# Generated by Django 4.0.4 on 2022-05-26 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_company_type_remove_consumer_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='cert1',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='cert2',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='cert3',
            field=models.BooleanField(default=False),
        ),
    ]
