# Generated by Django 3.1.7 on 2021-02-26 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent_id',
            field=models.IntegerField(blank=True),
        ),
    ]
