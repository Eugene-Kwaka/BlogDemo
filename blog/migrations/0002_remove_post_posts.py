# Generated by Django 3.2.9 on 2021-12-02 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='posts',
        ),
    ]
