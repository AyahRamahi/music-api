# Generated by Django 2.2.5 on 2019-09-11 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='name',
            new_name='song_name',
        ),
    ]