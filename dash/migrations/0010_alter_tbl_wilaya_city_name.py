# Generated by Django 4.0.4 on 2022-05-20 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0009_rename_geometry_tbl_wilaya_city_poly'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_wilaya',
            name='city_name',
            field=models.CharField(blank=True, max_length=35),
        ),
    ]