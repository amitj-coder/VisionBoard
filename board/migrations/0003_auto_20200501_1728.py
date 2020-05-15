# Generated by Django 3.0.5 on 2020-05-01 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20200501_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='vision',
        ),
        migrations.AddField(
            model_name='vision',
            name='file',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='board.Photo'),
            preserve_default=False,
        ),
    ]
