from django.contrib import admin
from .models import ContactQuery, WebTemplate, MobileTemplate

@admin.register(ContactQuery)
class ContactQueryAdmin(admin.ModelAdmin):
    list_display  = ['first_name','last_name','email','service','created_at','is_read']
    list_filter   = ['service','is_read','created_at']
    search_fields = ['first_name','last_name','email']
    list_editable = ['is_read']
    readonly_fields = ['created_at']

@admin.register(WebTemplate)
class WebTemplateAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','is_featured']
    list_filter  = ['category','is_featured']

@admin.register(MobileTemplate)
class MobileTemplateAdmin(admin.ModelAdmin):
    list_display = ['name','category','platform','price','is_featured']
    list_filter  = ['platform','is_featured']
