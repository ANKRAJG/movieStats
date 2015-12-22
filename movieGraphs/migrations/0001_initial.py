# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistImage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('artst_name', models.CharField(max_length=140)),
                ('artist_img', models.ImageField(upload_to='photos/artist_images')),
                ('artist_prof', models.CharField(max_length=150)),
                ('artist_gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hollywood',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('movie', models.CharField(max_length=140)),
                ('actors', models.TextField()),
                ('directors', models.CharField(max_length=140)),
                ('producers', models.TextField()),
                ('release', models.IntegerField()),
                ('rating', models.FloatField()),
                ('budget', models.IntegerField()),
                ('box_office', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieImage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=140)),
                ('movie_img', models.ImageField(upload_to='photos')),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('prof_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Xaxis',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('xaxis_value', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Yaxis',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('yaxis_value', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='prof',
            field=models.ForeignKey(to='movieGraphs.Profession'),
        ),
    ]
