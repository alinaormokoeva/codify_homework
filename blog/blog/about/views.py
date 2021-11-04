from django.shortcuts import render
from .forms import Information
from .models import About

# Create your views here.
def about(request):
    if request.method == 'POST':
        form = Information(request.POST)
        if form.is_valid():
            cd = form.cleaned_data  
            new_object = About(email=cd['email'],first_name = cd['first_name'],last_name= cd['last_name'],message= cd['message'],allow_mailing=cd['allow_mailing'])
            new_object.save()
            

    else:
        form = Information()
    return render(request, "about.html",{'form': form})
