# Generated by Django 4.1.5 on 2023-02-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='Nothing', upload_to='static/img'),
        ),
    ]
