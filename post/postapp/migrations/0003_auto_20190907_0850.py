# Generated by Django 2.2.4 on 2019-09-07 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0002_post_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postapp.Post')),
            ],
        ),
    ]
