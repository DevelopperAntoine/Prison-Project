# Generated by Django 4.0.4 on 2022-05-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='avatar.png', upload_to='photos/'),
        ),
    ]
