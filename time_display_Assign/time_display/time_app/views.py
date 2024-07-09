from django.shortcuts import render 
from datetime import datetime
def current_datetime(request):
    now = datetime.now()
    context = {
        'current_date': now.date(),
        'current_time': now.time(),
    }
    return render(request, 'time_app/current_datetime.html',context)

# Create your views here.
