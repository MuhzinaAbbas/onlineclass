# Generated by Django 5.1 on 2024-08-21 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stdimage',
            field=models.ImageField(upload_to='static/students/'),
        ),
    ]