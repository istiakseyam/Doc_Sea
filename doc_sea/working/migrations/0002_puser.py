# Generated by Django 4.0.2 on 2022-06-07 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('working', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('passwordk', models.CharField(max_length=20)),
            ],
        ),
    ]
