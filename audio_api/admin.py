from django.contrib import admin
from .models import audio_storage
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(audio_storage)
class audioAdmin(ImportExportModelAdmin):
    pass