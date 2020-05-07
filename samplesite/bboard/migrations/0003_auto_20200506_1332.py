# Generated by Django 3.0.3 on 2020-05-06 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20200506_0937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rubric',
            options={'ordering': ['name'], 'verbose_name': 'рубрика', 'verbose_name_plural': 'Рубрики'},
        ),
        migrations.RemoveField(
            model_name='bb',
            name='price',
        ),
        migrations.AddField(
            model_name='bb',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Артикл'),
        ),
    ]
