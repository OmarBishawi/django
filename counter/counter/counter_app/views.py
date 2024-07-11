# counter/views.py

from django.shortcuts import render, redirect

def index(request):
    if 'visit_count' not in request.session:
        request.session['visit_count'] = 0
    request.session['visit_count'] += 1
    context = {
        'visit_count': request.session['visit_count']
    }
    return render(request, 'counter_app/index.html', context)

def destroy_session(request):
    if 'visit_count' in request.session:
        del request.session['visit_count']
    return redirect('index')
