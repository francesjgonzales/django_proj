from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        """ fields = ['name', 'email', 'date', 'number_of_guests'] """
        fields = '__all__'  # This will include all fields from the model
        """ widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'date': 'Reservation Date and Time',
            'number_of_guests': 'Number of Guests',
        }
        help_texts = {
            'name': 'Enter your full name.',
            'email': 'We will send a confirmation to this email.',
        } """