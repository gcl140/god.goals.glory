# Generated by Django 5.1.6 on 2025-03-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuzzaz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures'),
        ),
    ]
