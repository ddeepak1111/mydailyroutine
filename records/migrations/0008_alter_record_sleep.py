# Generated by Django 4.2.2 on 2023-06-21 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0007_alter_record_gym_alter_record_reading_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='sleep',
            field=models.CharField(choices=[('1-3 Hrs', '1 to 3 hours scores 15'), ('3-5 Hrs', '3 to 5 hours scores 10'), ('5-7 Hrs', '5 to 7 hours scores 5'), ('7+ Hrs', 'Above 7 hours scores 0')], max_length=10),
        ),
    ]
