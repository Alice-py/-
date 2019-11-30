
from django.contrib import admin
from django.contrib import admin
from ksglapp.models import Stinfo,OpenDoor,AppleLog

class StinfoAdmin(admin.ModelAdmin):
    list_display = ['st_id','st_name','st_gender','st_college','st_major','st_class','st_position']

class OpenDooroAdmin(admin.ModelAdmin):
    list_display = ['fsid','sprofessional','sposition','spermissions']
    
class AppleLogAdmin(admin.ModelAdmin):
    list_display = ['stime','sid','sprofessional','sphone','sresults']
    
# class VerboseAdmin(admin.ModelAdmin):
#	list_display = ['']
	

admin.site.register(Stinfo,StinfoAdmin)
# admin.site.register()
admin.site.register(OpenDoor,OpenDooroAdmin)
admin.site.register(AppleLog,AppleLogAdmin)