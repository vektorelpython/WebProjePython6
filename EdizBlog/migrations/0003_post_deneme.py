# Generated by Django 2.1.7 on 2019-04-21 11:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EdizBlog', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='deneme',
            field=models.TextField(default=django.utils.timezone.now),
        ),
    ]
