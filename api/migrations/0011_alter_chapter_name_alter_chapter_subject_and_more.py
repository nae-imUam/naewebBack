# Generated by Django 5.0.1 on 2024-01-08 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_course_subject_chapter_subtopic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subject'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='subject',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('correct_answer', models.CharField(max_length=100)),
                ('options', models.JSONField()),
                ('chapter_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.chapter')),
                ('class_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.course')),
                ('subject_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.subject')),
            ],
        ),
        migrations.CreateModel(
            name='MiniTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subject')),
                ('questions', models.ManyToManyField(to='api.question')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('questions', models.ManyToManyField(related_name='question_sets', to='api.question')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.chapter')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='topic_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.topic'),
        ),
        migrations.DeleteModel(
            name='SubTopic',
        ),
    ]
