from django.contrib import admin
from .models import Album, Image, Video,News
from django_ckeditor_5.widgets import CKEditor5Widget
from django.db import models
from django.utils.html import format_html



class ImageInline(admin.TabularInline):  # Hoặc dùng StackedInline nếu muốn giao diện khác
    model = Image
    extra = 3  # Hiển thị sẵn 3 ô tải ảnh (có thể chỉnh số này)
    fields = ['file', 'title']
    verbose_name = "Hình ảnh"
    verbose_name_plural = "Danh sách hình ảnh"

class AlbumAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    inlines = [ImageInline]  # Thêm Inline vào AlbumAdmin

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_preview', 'created_at')
    formfield_overrides = {
        models.TextField: {"widget": CKEditor5Widget(config_name="default")},
    }

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" width="80" height="auto" style="border-radius:5px;">', obj.thumbnail.url)
        return "Không có ảnh"
    thumbnail_preview.short_description = "Thumbnail"


    

admin.site.register(News, NewsAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Video)  # Đăng ký Video
