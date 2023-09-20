from django.contrib import admin
from .models import *

# Register your models here.
class LandDetailsAdmin(admin.ModelAdmin):
    list_display = ("id", "latitude", "longitude")
admin.site.register(LandDetails, LandDetailsAdmin)

class ETRSAdmin(admin.ModelAdmin):
    list_display= ("tree_id_id", "tree_name")
admin.site.register(ETRS, ETRSAdmin)

class CTRSAdmin(admin.ModelAdmin):
    list_display = ("tree_id_id", "tree_name")
admin.site.register(CTRS, CTRSAdmin)

