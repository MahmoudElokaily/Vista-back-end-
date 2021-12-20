from .models import *
from django import forms

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widget = {
            'name' : forms.TextInput(),
            'mail': forms.EmailInput(),
            'password': forms.TextInput(),
            'phone' : forms.TextInput(),
            'age' : forms.NumberInput(),
            'address' : forms.TextInput(),
            'photo' : forms.FileInput(),
            'major' : forms.TextInput(),
            'cost' : forms.TextInput(),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widget = {
            'name' : forms.TextInput(),
            'mail' : forms.EmailInput(),
            'password' : forms.TextInput(),
            'age' : forms.IntegerField(),
            'phone' : forms.TextInput(),
            'address' : forms.TextInput(),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = [
            'name_of_hospital',
            'year_of_experience',
        ]
        widget = {
            'name_of_hospital' : forms.TextInput(),
            'year_of_experience' : forms.NumberInput(),
        }






class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
             'date',
             'time',
             'Doctor',
        ]
        widget = {
            'date' : forms.DateInput(),
            'time' : forms.TimeInput(),
            'Doctor' : forms.Select(),
        }