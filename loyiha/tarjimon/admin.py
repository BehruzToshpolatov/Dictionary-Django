from django.contrib import admin
from .models import Lugat
# Register your models here.
class LugatAdmin(admin.ModelAdmin):
    list_display = ['english', 'uzbek']

admin.site.register(Lugat, LugatAdmin)