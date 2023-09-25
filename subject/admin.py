from django.contrib import admin

# Register your models here.

from django.contrib import admin
from . import models

#registered models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category'
    ]
    
@admin.register(models.subject)
class subjectAdmin(admin.ModelAdmin):
    list_display = [
        'class_id',
        'class_name',
        'class_category',
        'on_register',
    ]