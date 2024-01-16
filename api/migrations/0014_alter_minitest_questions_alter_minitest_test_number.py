# Generated by Django 5.0.1 on 2024-01-10 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_remove_minitest_date_minitest_test_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minitest',
            name='questions',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='minitest',
            name='test_number',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]