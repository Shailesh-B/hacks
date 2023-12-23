# Generated by Django 4.2.8 on 2023-12-23 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('current_price', models.IntegerField(default=0)),
                ('quantity_sold', models.IntegerField(default=0)),
            ],
        ),
    ]
