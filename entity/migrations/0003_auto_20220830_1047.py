# Generated by Django 3.2.15 on 2022-08-30 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0002_auto_20220818_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='description',
            field=models.CharField(default=3, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='branch',
            name='code',
            field=models.CharField(max_length=30),
        ),
    ]
