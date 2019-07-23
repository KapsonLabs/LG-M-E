# Generated by Django 2.2.3 on 2019-07-16 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=100)),
                ('district_region', models.CharField(choices=[('NORTHERN', 'NORTHERN'), ('WESTERN', 'WESTERN'), ('CENTRAL', 'CENTRAL'), ('EASTERN', 'EASTERN'), ('WESTNILE', 'WESTNILE')], max_length=20)),
                ('district_size_hectares', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
