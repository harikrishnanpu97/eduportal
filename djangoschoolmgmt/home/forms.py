from django import forms
from .models import Registration
from .models import ContactSubmission



class DateInput(forms.DateInput):
    input_type = 'date'

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'booking_date': DateInput(),  
        }

        labels = {
            's_name': "Student Name",
            's_phone': "Student Phone", 
            's_email': "Student Email", 
            'dep_name': "Department Name",
            'booking_date': "Booking Date",
        }
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']