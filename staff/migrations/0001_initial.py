# Generated by Django 5.1.6 on 2025-03-07 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('sold_out', 'Sold Out'), ('on_production', 'On Production')], default='available', max_length=20)),
                ('quantity', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
    ]
