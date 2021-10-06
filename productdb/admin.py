from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import product_details
# Register your models here.

@admin.register(product_details)
class PersonAdmin(ImportExportActionModelAdmin):
    pass