# Generated by Django 3.0.3 on 2020-05-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_auto_20200506_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads_photo/%Y/%m/%d/'),
        ),
    ]
