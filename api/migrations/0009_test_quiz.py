# Generated by Django 5.0.1 on 2024-01-08 02:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_delete_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testNumber', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('options', models.JSONField()),
                ('correctOption', models.CharField(max_length=50)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.test')),
            ],
        ),
    ]
