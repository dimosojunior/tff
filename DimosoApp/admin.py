from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from DimosoApp.models import *


# Register your models here.

class TeamsAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]

class TeamInformationsAdmin(admin.ModelAdmin):
	list_display = ["prayer_name", "team_name", "total_goals", "total_assists", "total_yellow", "total_red"]
class MsimamoAdmin(admin.ModelAdmin):
	list_display = ["name", "title", "playing_date"]

class RatibaAdmin(admin.ModelAdmin):
	list_display = ["playing_date", "title", "playing_date"]

class ResultsAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date", "title", "playing_date"]


admin.site.register(Teams, TeamsAdmin)
admin.site.register(TeamInformations, TeamInformationsAdmin)
admin.site.register(Msimamo, MsimamoAdmin)
admin.site.register(Ratiba, RatibaAdmin)
admin.site.register(Results, ResultsAdmin)

