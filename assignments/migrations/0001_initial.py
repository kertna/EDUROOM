# Generated by Django 3.2.7 on 2021-11-27 06:56

import datetime
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
            name='Submissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('code', models.IntegerField()),
                ('solution_file', models.FileField(upload_to='solutions/')),
                ('marks', models.IntegerField(null=True)),
                ('comment', models.TextField(null=True)),
                ('is_copied', models.BooleanField(null=True)),
                ('submission_time', models.DateField(default=datetime.datetime.now)),
                ('student_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentDiscussion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('code', models.IntegerField()),
                ('message_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('message', models.TextField()),
                ('student_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('code', models.IntegerField(help_text='Unique Code', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('deadline', models.DateField()),
                ('question_file', models.FileField(upload_to='questions/')),
                ('maximum_marks', models.PositiveIntegerField()),
                ('creator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
