# Generated by Django 2.2 on 2019-05-30 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20190525_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='image',
            field=models.ImageField(default=1, upload_to='field/images'),
            preserve_default=False,
        ),
    ]
