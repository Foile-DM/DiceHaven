from django.db import models
from datetime import timedelta, date, datetime, time


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


class BookingTime(models.Model):
    user_phone = models.CharField('Телефон', max_length=255, blank=True, null=True)
    game_system = models.ForeignKey(Game, on_delete=models.CASCADE, blank=True, null=True)
    game_master = models.ForeignKey(GameMaster, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField('Дата')
    start_time = models.TimeField('Начало')
    end_time = models.TimeField('Конец')
    is_available = models.BooleanField('Бронь', default=True)

    @classmethod
    def generate_bookings(cls):
        start_date = date.today()
        end_date = start_date + timedelta(days=21)

        # Генерируем записи на пятницу, субботу и воскресенье
        current_date = start_date
        while current_date <= end_date:
            if current_date.weekday() in [4, 5, 6]:  # Проверяем, является ли день пятницей, субботой или воскресеньем
                # Проверяем наличие записей для каждого временного интервала
                start_time = datetime.combine(current_date, time(hour=9))  # Начало работы
                end_time = datetime.combine(current_date, time(hour=18))  # Конец работы

                # Генерируем записи с интервалом в 1 час, если записей нет
                while start_time < end_time:
                    if not cls.objects.filter(date=current_date, start_time=start_time.time()).exists():
                        cls.objects.create(date=current_date, start_time=start_time.time(),
                                           end_time=(start_time + timedelta(hours=1)).time())
                    start_time += timedelta(hours=1)

            current_date += timedelta(days=1)
