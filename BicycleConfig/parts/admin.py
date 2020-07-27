from django.contrib import admin
from .models import *



class PartsAdmin(admin.ModelAdmin):
    list_display = ('Parts_name', 'Parts_price', 'Parts_description', 'start_date')
    empty_value_display = '-empty-'
    list_filter = ('Parts_name', 'start_date')
    list_per_page = 25
    ordering = ['Parts_name']

admin.site.register(Parts, PartsAdmin)