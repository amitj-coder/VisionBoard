# Generated by Django 3.0.8 on 2020-08-01 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0014_auto_20200801_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vision',
            name='image',
            field=models.ImageField(default='default.jpg', help_text='Profile Picture', upload_to='', verbose_name='Profile Picture'),
        ),
    ]
