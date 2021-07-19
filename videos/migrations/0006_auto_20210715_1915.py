# Generated by Django 3.2.5 on 2021-07-15 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_videoallproxy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VideoProxy',
        ),
        migrations.CreateModel(
            name='VideoPublishedProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Piblished Video',
                'verbose_name_plural': 'Piblished Videos',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('videos.video',),
        ),
    ]
