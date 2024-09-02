from django import forms
from .models import Booking
class DateInput(forms.DateInput):
    input_type = 'date'
class Bookingform(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets={
           'book_date':DateInput()
        }
        labels={
            'pati_name':"Patient name:",
            'pati_phone': "Phone number:",
            'pati_email': "E-mail:",
            'dep_name':"Department:",
            'doc_name':"Doctor:",
            'book_date':"Booking Date:"
        }
