# Generated by Django 4.2.2 on 2023-07-03 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_alter_post_art_alter_post_love'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='art',
            field=models.ImageField(upload_to=''),
        ),
    ]