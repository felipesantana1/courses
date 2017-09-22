# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 21:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0005_auto_20170922_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='desc',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='desc',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='desc', to='courses_app.Courses'),
        ),
    ]
