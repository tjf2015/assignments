# Generated by Django 2.2.4 on 2020-12-15 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]
