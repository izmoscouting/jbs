from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from.models import Player, Scout, Business, Club, Agency, Coach, Contact



class PlayerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
    
admin.site.register(Player,PlayerAdmin)

class ScoutAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
    

admin.site.register(Scout,ScoutAdmin)

class BusinessAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
    

admin.site.register(Business,BusinessAdmin)


class ClubAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
    

admin.site.register(Club,ClubAdmin)

class AgencyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
    
admin.site.register(Agency,AgencyAdmin)


class CoachAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
    
admin.site.register(Coach,CoachAdmin)

class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
    
admin.site.register(Contact,ContactAdmin)