# Generated by Django 3.2 on 2022-11-01 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_rename_icons_skils_image_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='skils',
            name='url_icon',
            field=models.TextField(default=True),
        ),
    ]