# Generated by Django 4.0.4 on 2022-05-20 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0008_alter_tbl_wilaya_city_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_wilaya',
            old_name='geometry',
            new_name='city_poly',
        ),
    ]
