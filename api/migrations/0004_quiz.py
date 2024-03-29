# Generated by Django 5.0.1 on 2024-01-07 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_userprofile_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('options', models.JSONField()),
                ('correct_option', models.CharField(max_length=255)),
            ],
        ),
    ]
