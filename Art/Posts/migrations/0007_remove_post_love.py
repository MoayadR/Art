# Generated by Django 4.2.2 on 2023-07-21 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0006_delete_profile_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='love',
        ),
    ]
