# Generated by Django 2.2.4 on 2019-08-24 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_level', models.IntegerField()),
                ('total_classes', models.IntegerField(default=0)),
                ('attended_classes', models.IntegerField(default=0)),
                ('discussion_score', models.IntegerField(default=0)),
                ('prediction_score', models.IntegerField(default=2)),
                ('mentor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
