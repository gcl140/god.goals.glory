# Generated by Django 5.1.6 on 2025-03-09 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_testimonial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='stars',
        ),
    ]
