# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-11 11:44
from __future__ import unicode_literals

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
            name='Sto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='sto_logo/')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sto', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
