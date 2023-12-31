# Generated by Django 4.2.2 on 2023-06-20 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_record_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='water_intake',
            field=models.CharField(choices=[('3L', '3L scores 3'), ('2L', '3L scores 2'), ('1L', '3L scores 1')], default=2, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='score',
            name='water_intake_score',
            field=models.IntegerField(default=0),
        ),
    ]
