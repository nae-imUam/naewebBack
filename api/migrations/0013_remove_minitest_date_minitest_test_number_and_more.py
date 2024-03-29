# Generated by Django 5.0.1 on 2024-01-10 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_minitest_class_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='minitest',
            name='date',
        ),
        migrations.AddField(
            model_name='minitest',
            name='test_number',
            field=models.PositiveIntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='minitest',
            name='class_name',
            field=models.CharField(max_length=50),
        ),
        migrations.RemoveField(
            model_name='minitest',
            name='questions',
        ),
        migrations.AlterField(
            model_name='minitest',
            name='subject',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='minitest',
            name='questions',
            field=models.JSONField(null=True),
        ),
    ]
