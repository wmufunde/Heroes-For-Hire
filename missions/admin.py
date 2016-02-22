from django.contrib import admin
from .models import Hero, Team, Customer, Mission, Alias, HeroStatus, Report

# Register your models here.

admin.site.register(Hero)
admin.site.register(Team)
admin.site.register(Customer)
admin.site.register(Mission)
admin.site.register(Alias)
admin.site.register(HeroStatus)
admin.site.register(Report)
