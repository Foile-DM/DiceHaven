from django.contrib import admin
from .models import GameMaster, Game, BookingTime

admin.site.register(GameMaster)
admin.site.register(Game)
admin.site.register(BookingTime)
