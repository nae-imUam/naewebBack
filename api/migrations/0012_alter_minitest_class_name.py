# Generated by Django 5.0.1 on 2024-01-08 19:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_chapter_name_alter_chapter_subject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minitest',
            name='class_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course'),
        ),
    ]