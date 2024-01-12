from django.contrib import admin
from .models import Doctor,Specialization,Designation, AvailableTime,Review
# Register your models here.
admin.site.register(Doctor)
class SpacializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


class DesignationionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Specialization, SpacializationAdmin)
admin.site.register(AvailableTime)
admin.site.register(Designation,DesignationionAdmin)
admin.site.register(Review)