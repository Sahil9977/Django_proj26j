from django.contrib import admin

from .models import Note

# admin.site.register(Note)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display=('id','title','description')

admin.site.site_header="Angaari Notes"

# Register your models here.
