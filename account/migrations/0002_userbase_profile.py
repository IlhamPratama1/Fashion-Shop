# Generated by Django 3.2.3 on 2021-08-30 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbase',
            name='profile',
            field=models.ImageField(default='images/ava.jpg', upload_to='images/'),
        ),
    ]
