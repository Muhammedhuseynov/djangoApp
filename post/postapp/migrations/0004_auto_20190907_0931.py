# Generated by Django 2.2.4 on 2019-09-07 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0003_auto_20190907_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(default='user.jpg', upload_to='media'),
        ),
    ]
