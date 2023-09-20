from django.db import models
from datetime import timedelta, date, datetime, time


class GameMaster(models.Model):
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    tg_username = models.CharField('Телеграм', max_length=255)
    phone_number = models.CharField('Телефон', max_length=255)
    photo = models.ImageField('Фото', upload_to='static/main/img/DM', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}"


class Game(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField("Описание", blank=True, null=True)

    def __str__(self):
        return self.name


TIME_CHOICES = (
    ("17:00 - 19:30", "17:00-19:30"),
    ("20:00 - 22:30", "20:00-22:30"),
)


class BookingTime(models.Model):
    user_phone = models.CharField('Телефон', max_length=15, blank=True, null=True)
    user_name = models.CharField('Имя', max_length=255, blank=True, null=True)
    game_system = models.ForeignKey(Game, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField('Дата')
    time = models.CharField('Время', max_length=20, choices=TIME_CHOICES, default="17:00 - 19:30")

    def __str__(self):
        return f"{self.date}, {self.time}"


