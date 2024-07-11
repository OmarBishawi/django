from django.shortcuts import render, redirect
from django.http import HttpResponse
import random

def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['attempts'] = 0
    return render(request, 'numbers_app/index.html')

def guess(request):
    guess = int(request.POST['guess'])
    number = request.session['number']
    request.session['attempts'] += 1

    if guess < number:
        message = "Too low!"
        color = "blue"
    elif guess > number:
        message = "Too high!"
        color = "red"
    else:
        message = f"Correct! You guessed the number in {request.session['attempts']} attempts."
        color = "green"

    context = {
        'message': message,
        'color': color,
        'guessed_correctly': guess == number,
    }

    return render(request, 'numbers_app/index.html', context)

def reset(request):
    request.session.flush()
    return redirect('index')

# Create your views here.
