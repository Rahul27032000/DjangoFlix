# Generated by Django 3.1.7 on 2021-07-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_alter_video_video_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
