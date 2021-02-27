from django.shortcuts import render, redirect
from .models import Band

# Create your views here.
def create(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        style = request.POST['style']
        location = request.POST['location']

        ins = Band(name=name, description=description,
                style=style, location=location)
        ins.save()
        return redirect('dashboard')


    return render(request, 'band/create.html')