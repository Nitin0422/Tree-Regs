from django.contrib import admin
from .models import *

# Register your models here.
class ETRSAdmin(admin.ModelAdmin):
    fields = ('tree_id', 'name')

admin.site.register(LandDetails)
admin.site.register(ETRS, ETRSAdmin)
admin.site.register(CTRS)

