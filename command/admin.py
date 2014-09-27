from django.contrib import admin
from command.models import Command

class CommandAdmin(admin.ModelAdmin):
    list_display = ['action', 'guy', 'issued_by', 'time_issued']

admin.site.register(Command, CommandAdmin)
