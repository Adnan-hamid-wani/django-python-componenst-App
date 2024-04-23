from django.shortcuts import render, redirect

# Create your views here.

from .forms import Travel


def travelform(request):
    if request.method == 'POST':
        form = Travel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('travel_success.html')
        else:
            form = Travel()
            return render(request, 'travel_form.html')
