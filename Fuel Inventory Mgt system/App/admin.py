from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header=("Admin Fuel Update by Njeri")
admin.site.register(Stock)
admin.site.register(Calculation)
