# Generated by Django 5.2.1 on 2025-05-12 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0039_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='detail',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
