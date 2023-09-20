from django import forms
from .models import BookingTime
from django.forms import ModelForm, DateInput


class BookingTimeForm(ModelForm):
    date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = BookingTime
        fields = ['user_phone', 'user_name', 'game_system', 'date', 'time']
