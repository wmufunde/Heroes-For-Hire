from django.contrib import admin
from .models import Team, Customer, Mission, Report

# Register your models here.

admin.site.register(Team)
admin.site.register(Customer)
admin.site.register(Mission)
admin.site.register(Report)
