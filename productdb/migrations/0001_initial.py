# Generated by Django 3.2.7 on 2021-09-15 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_number', models.IntegerField()),
                ('product_name', models.CharField(max_length=50)),
                ('product_mrp', models.IntegerField()),
                ('product_description', models.TextField()),
            ],
        ),
    ]
