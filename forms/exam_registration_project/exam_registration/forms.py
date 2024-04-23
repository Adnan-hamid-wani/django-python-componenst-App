from django import forms


class ExamRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Full Name')
    email = forms.EmailField(label='Email')
    father_name = forms.CharField(max_length=100, label='Fathers Name')
    mother_name = forms.CharField(max_length=100, label='Mothers Name')
    gender = forms.ChoiceField(label='Gender')
    date_of_birth = forms.DateField(label='DOB')
    address = forms.CharField(max_length=100, label='Address')
    state = forms.CharField(max_length=100, label='state')
    country = forms.CharField(max_length=100, label='Country')
    contact = forms.IntegerField(label='Contact')
    qualification = forms.CharField(max_length=100, label='qualification')
    photo = forms.ImageField(label='photo')
    signature = forms.ImageField(label='Signature')
    declaration = forms.BooleanField(label='I agree')
