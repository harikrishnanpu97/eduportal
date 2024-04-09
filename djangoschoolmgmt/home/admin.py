from django.contrib import admin
from .models import Department, Registration
from .models import ContactSubmission


admin.site.register(Department)

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['id', 's_name', 's_phone', 's_email', 'booking_date', 'booked_on', 'dep_name']

admin.site.register(Registration, RegistrationAdmin)

admin.site.register(ContactSubmission)

