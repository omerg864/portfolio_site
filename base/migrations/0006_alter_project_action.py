# Generated by Django 3.2.8 on 2021-12-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20211217_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='action',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]