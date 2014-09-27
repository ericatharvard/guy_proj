from django.contrib import admin
from guy.models import Guy
from command.models import Command
from position.models import Position

class CommandHistoryInline(admin.TabularInline):
    model = Command

class PositionInline(admin.StackedInline):
    model = Position

class GuyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
"""    inlines = [
        PositionInline,
        CommandHistoryInline
        ]
"""

admin.site.register(Guy, GuyAdmin)
