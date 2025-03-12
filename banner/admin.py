from django.contrib import admin
from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    search_fields = ('title',)
    list_filter = ('is_active',)
