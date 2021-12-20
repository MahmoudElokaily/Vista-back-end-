from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Experience)
admin.site.register(Client)
admin.site.register(Booking)