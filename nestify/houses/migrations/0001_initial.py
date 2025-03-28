# Generated by Django 5.1.6 on 2025-03-24 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HouseListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('sell', 'For Sale'), ('rent', 'For Rent')], max_length=10)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('images', models.JSONField(default=list)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('furnitured', models.BooleanField(default=False)),
                ('nearby_amenities', models.JSONField(default=list)),
            ],
        ),
    ]
