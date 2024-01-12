from django.contrib import admin
from .models import Appointment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctorname', 'patientname','appointment_types','appointment_status','symptom','time','cancel']

    
    def doctorname(self, obj):
        return obj.doctor.user.first_name
    def patientname(self, obj):
        return obj.patinet.user.first_name
    
    def save_model(self, request, obj, form, change):
        obj.save()
        if  obj.appointment_status == "Running" and obj.appointment_types == "Online":
            email_subject = "Your Appointment about to running"
            email_body = render_to_string('admin_email.html', {'user':obj.patinet.user,'doctor':obj.doctor})
            email = EmailMultiAlternatives(email_subject,'',to=[obj.patinet.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()


admin.site.register(Appointment, AppointmentAdmin)

