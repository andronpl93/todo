# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Название', max_length=100)),
                ('description', models.TextField(verbose_name='Подробное описание', blank=True, max_length=500)),
                ('img', models.IntegerField(verbose_name='Спрайт. Из одмена не использовать', default=15)),
                ('auth', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Краткое описание', max_length=100)),
                ('desctiption', models.TextField(verbose_name='Информация полезная для задачи(напр. телефоны, адреса, список продуктов)', blank=True, max_length=500)),
                ('date', models.DateTimeField(verbose_name='Время до которого нужно выполнить задачу')),
                ('status', models.BooleanField(verbose_name='Статус. Из одмена не использовать', default=False)),
                ('project', models.ForeignKey(to='apka.Projects')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
    ]
