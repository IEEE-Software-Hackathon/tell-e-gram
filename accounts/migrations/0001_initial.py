# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-23 18:01
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseId', models.CharField(max_length=8)),
                ('CourseName', models.CharField(max_length=250)),
                ('Credit', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FacultyID', models.CharField(max_length=8, unique=True)),
                ('Name', models.CharField(max_length=50)),
                ('Department', models.IntegerField()),
                ('Designation', models.IntegerField()),
                ('ContactNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Semester', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Course')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentID', models.CharField(max_length=8, unique=True)),
                ('Name', models.CharField(max_length=50)),
                ('Branch', models.IntegerField()),
                ('YearOfStudy', models.IntegerField()),
                ('ContactNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Semester', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Course')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='Courses',
            field=models.ManyToManyField(through='accounts.StudentCourse', to='accounts.Course'),
        ),
        migrations.AddField(
            model_name='student',
            name='User',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='faculty',
            name='Courses',
            field=models.ManyToManyField(through='accounts.FacultyCourse', to='accounts.Course'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='User',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
