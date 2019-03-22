from django.contrib import admin
from familydata.models import *
# Register your models here.


class FamilyAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'date_of_birth']
    list_filter = ['name', 'surname', 'date_of_birth']


admin.site.register(Family, FamilyAdmin)
admin.site.register(Posittion)
admin.site.register(FamilyApply)
admin.site.register(Package)