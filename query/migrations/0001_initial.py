# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-23 18:01
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
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AnswerTitle', models.TextField()),
                ('AnsweredAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuestionTitle', models.TextField()),
                ('AskedAt', models.DateTimeField(auto_now=True)),
                ('IsAnswered', models.BooleanField(default=False)),
                ('QueriedBy', models.CharField(default=None, max_length=100)),
                ('CreatedFor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='Question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='query.Question'),
        ),
    ]
