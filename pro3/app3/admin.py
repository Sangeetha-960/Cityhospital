from django.contrib import admin
from .models import department,Doctors,Booking
admin.site.register(department)
admin.site.register(Doctors)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','pati_name','pati_phone','pati_email','dep_name','doc_name','book_date','booked_on')
admin.site.register(Booking,BookingAdmin)