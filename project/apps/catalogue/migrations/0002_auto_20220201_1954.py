# Generated by Django 3.1.5 on 2022-02-01 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsattributevalue',
            name='value_option',
            field=models.ManyToManyField(to='catalogue.AttributeOption'),
        ),
    ]