from django.contrib import admin
from .models import Trainer, Class_Training, ReportLog, Attendance, Room, Hero
# Register your models here.

admin.site.register(Trainer)
admin.site.register(Class_Training)
admin.site.register(ReportLog)
admin.site.register(Attendance)
admin.site.register(Room)
admin.site.register(Hero)
