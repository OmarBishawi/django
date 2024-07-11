from django.shortcuts import render
def index(request):
    return render(request, "index.html")
def result(request):
    if request.method == 'POST' :
        data = request.POST
    return render(request, 'result.html', {'data' : data})
    return render(request, 'result.html')
   
