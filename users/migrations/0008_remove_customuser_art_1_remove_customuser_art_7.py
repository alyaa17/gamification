# Generated by Django 4.1.5 on 2023-03-04 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_customuser_art_1_customuser_art_2_customuser_art_3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='art_1',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='art_7',
        ),
    ]