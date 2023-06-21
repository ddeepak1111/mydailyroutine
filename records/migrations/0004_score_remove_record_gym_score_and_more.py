# Generated by Django 4.2.2 on 2023-06-19 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_record_gym_score_record_reading_score_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='records.record')),
                ('sleep_score', models.IntegerField(default=0)),
                ('yoga_score', models.IntegerField(default=0)),
                ('gym_score', models.IntegerField(default=0)),
                ('walking_score', models.IntegerField(default=0)),
                ('reading_score', models.IntegerField(default=0)),
                ('skills_development_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='record',
            name='gym_score',
        ),
        migrations.RemoveField(
            model_name='record',
            name='reading_score',
        ),
        migrations.RemoveField(
            model_name='record',
            name='skills_development_score',
        ),
        migrations.RemoveField(
            model_name='record',
            name='sleep_score',
        ),
        migrations.RemoveField(
            model_name='record',
            name='walking_score',
        ),
        migrations.RemoveField(
            model_name='record',
            name='yoga_score',
        ),
    ]