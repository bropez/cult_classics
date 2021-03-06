# Generated by Django 2.2.2 on 2019-06-22 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_auto_20190622_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='acted_in',
        ),
        migrations.RemoveField(
            model_name='director',
            name='directed_in',
        ),
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.ManyToManyField(blank=True, to='films.Actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ManyToManyField(blank=True, to='films.Director'),
        ),
    ]
