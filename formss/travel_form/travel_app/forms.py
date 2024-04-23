from django import forms
from .models import Travel


class BookingForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = '__all__'
