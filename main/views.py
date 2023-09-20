from django.shortcuts import render, redirect
from .forms import BookingTimeForm
from .models import Game, BookingTime, GameMaster
from django.contrib import messages


def home(request):
    masters = GameMaster.objects.all()
    data = {
        'masters': masters
    }
    return render(request, "main/home.html", data)


def about(request):
    return render(request, "main/about.html")


def reservation(request):

    form = BookingTimeForm
    data = {
        'form': form
    }

    if request.method == 'POST':
        user_phone = request.POST.get('user_phone')
        user_name = request.POST.get('user_name')
        game_system = request.POST.get('game_system')
        date = request.POST.get('date')
        time = request.POST.get('time')
        if not user_phone:
            messages.success(request, "Не введен телефон")
            return redirect('reservation')
        if not user_name:
            messages.success(request, "Не введено имя")
            return redirect('reservation')
        if not game_system:
            messages.success(request, "Выбери игровую систему")
            return redirect('reservation')

        request.session['user_phone'] = user_phone
        request.session['user_name'] = user_name
        request.session['game_system'] = game_system
        request.session['date'] = date
        request.session['time'] = time

        return redirect('reservation_submit')

    return render(request, 'main/reservation.html', data)


def reservation_submit(request):

    user_phone = request.session.get('user_phone')
    user_name = request.session.get('user_name')
    game_system_id = request.session.get('game_system')
    game_system = Game.objects.get(id=game_system_id)
    date = request.session.get('date')
    time = request.session.get('time')

    if BookingTime.objects.filter(date=date, time=time).count() < 1:
        BookingTime.objects.get_or_create(
            user_phone=user_phone,
            user_name=user_name,
            game_system=game_system,
            date=date,
            time=time
        )
        messages.success(request, "Запись сохранена!")
        return redirect('home')

    else:
        messages.success(request, "Это время уже занято")
        return redirect('reservation')


def contact(request):
    return render(request, "main/contact.html")
