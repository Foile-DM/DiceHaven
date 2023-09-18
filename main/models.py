from django.db import models


class GameMaster(models.Model):
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    middle_name = models.CharField('Отчество', max_length=255, blank=True, null=True)
    tg_username = models.CharField('Телеграм', max_length=255)
    phone_number = models.CharField('Телефон', max_length=255)
    game_systems = models.ManyToManyField('Game', verbose_name='Игровые системы', blank=True)
    photo = models.ImageField('Фото', upload_to='static/img/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}"


class Game(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField("Описание", blank=True, null=True)

    def __str__(self):
        return self.name
