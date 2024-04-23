from django.shortcuts import render, redirect

# Create your views here.
from .forms import ExamRegistrationForm


def exam_registration(request):
    if request.method == 'POST':
        form = ExamRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('success')
        else:
            form = ExamRegistrationForm()
            return render(request, 'exam_registration,html', {'form': form})


def success_view():
    return None
