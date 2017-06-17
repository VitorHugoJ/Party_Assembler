# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-17 21:56
from __future__ import unicode_literals

import PartyAssembler.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Enter_party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Name', max_length=50)),
                ('game_cover', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=PartyAssembler.models.upload_location, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('description', models.TextField(default='')),
                ('party_img', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=PartyAssembler.models.upload_location, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('leader', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('related_game', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='PartyAssembler.Game')),
            ],
        ),
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=PartyAssembler.models.upload_location, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('idt', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='enter_party',
            name='party_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='PartyAssembler.Party'),
        ),
        migrations.AddField(
            model_name='enter_party',
            name='usr_nickname',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
