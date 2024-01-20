from django.shortcuts import render

# Create your views here.

from app.forms import*

def reg(request):
    ufo=UserForm()
    pfo=ProfileForm()

    D={'ufo':ufo,'pfo':pfo}

    return render(request,'reg.html',D)