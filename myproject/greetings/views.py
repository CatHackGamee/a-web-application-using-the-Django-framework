from django.shortcuts import render, redirect
from .models import UserName

def index(request):
    last_user = UserName.objects.last()
    greeting = None
    error = None

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()

        if not name:
            error = 'Пожалуйста, введите имя!'
        else:
            UserName.objects.create(name=name)
            return redirect('index')

    if last_user and request.method == 'GET':
        greeting = f'Привет, {last_user.name}!'

    return render(request, 'greetings/index.html', {
        'greeting': greeting,
        'error': error,
    })