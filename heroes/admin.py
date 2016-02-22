from django.contrib import admin
from .models import Hero, Alias, HeroStats, HeroStatus


# Register your models here.
admin.site.register(Hero)
admin.site.register(Alias)
admin.site.register(HeroStats)
admin.site.register(HeroStatus)
