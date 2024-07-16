from django.shortcuts import render, redirect
import random

def index(request):
    if 'ninja_gold' not in request.session:
        request.session['ninja_gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html', {
        'ninja_gold': request.session['ninja_gold'],
        'activities': request.session['activities']
    })

def process_money(request):
    locations = {
        'farm': (10, 20),
        'cave': (5, 10),
        'house': (2, 5),
        'casino': (-50, 50)
    }

    if request.method == 'POST':
        location = request.POST['building']
        earnings_range = locations.get(location)
        if earnings_range:
            earnings = random.randint(*earnings_range)
            request.session['ninja_gold'] += earnings

            activity = ''
            if earnings >= 0:
                activity = f'Earned {earnings} gold from the {location}!'
            else:
                activity = f'Entered a casino and lost {-earnings} gold... Ouch...'
            
            request.session['activities'].append(activity)
            request.session.modified = True

    return redirect('/')
