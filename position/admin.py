from django.contrib import admin
from position.models import Position

class PositionAdmin(admin.ModelAdmin):
    fields = ['x', 'y', 'dir']
    list_display = ['x', 'y', 'dir']

admin.site.register(Position, PositionAdmin)
