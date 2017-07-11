from django.contrib import admin
from .models import Remainder

class RemainderAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Remainder, RemainderAdmin)