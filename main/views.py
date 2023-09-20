from django.shortcuts import render, redirect
from .forms import BookingTimeForm
from django.contrib import messages


def home(request):
    return render(request, "main/home.html")


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
            messages.success(request, "Напиши телефон")
            return redirect('reservation')
        if not user_name:
            messages.success(request, "Напиши имя")
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
    return render(request, 'main/reservation_submit.html')


def contact(request):
    return render(request, "main/contact.html")

