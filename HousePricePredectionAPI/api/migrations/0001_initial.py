# Generated by Django 4.1.8 on 2023-07-05 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.IntegerField(default=0)),
                ('bedrooms', models.IntegerField(default=0)),
                ('bathrooms', models.IntegerField(default=0)),
                ('stories', models.IntegerField(default=0)),
                ('mainroad', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('guestroom', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('basement', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('hotwaterheating', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('airconditioning', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('parking', models.IntegerField(default=0)),
                ('prefarea', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('semi_furnished', models.CharField(choices=[('Semi_furnished', 'Semi_furnished'), ('Unurnished', 'Unfurnished')], max_length=15)),
                ('unfurnished', models.CharField(choices=[('Semi_furnished', 'Semi_furnished'), ('Unurnished', 'Unfurnished')], max_length=15)),
            ],
        ),
    ]
