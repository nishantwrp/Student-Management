# Generated by Django 2.2.4 on 2019-08-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.TextField(default='Test User'),
            preserve_default=False,
        ),
    ]
