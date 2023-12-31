# Generated by Django 4.2.5 on 2023-09-18 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='GameMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество')),
                ('tg_username', models.CharField(max_length=255, verbose_name='Телеграм')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Телефон')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/img/', verbose_name='Фото')),
                ('game_systems', models.ManyToManyField(blank=True, to='main.game', verbose_name='Игровые системы')),
            ],
        ),
    ]
