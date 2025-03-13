from django.contrib import admin
from .models import Applicant, Job
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms
from django.utils.safestring import mark_safe
from unidecode import unidecode
from django.db.models import Q
from .models import EmailTemplate
from django.db import models

# Tạo form để sử dụng CKEditor5 trong Admin
class JobAdminForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        widgets = {
            'benefits': CKEditor5Widget(config_name='extends'),
            'requirements': CKEditor5Widget(config_name='extends'),
            'description': CKEditor5Widget(config_name='extends'),
            'rights': CKEditor5Widget(config_name='extends'),
        }

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    form = JobAdminForm
    list_display = ('id', 'title', 'slug', 'specialty', 'expertise', 'location', 'job_type', 'salary', 'deadline')
    search_fields = ('title', 'specialty', 'expertise', 'location', 'slug')
    list_filter = ('job_type', 'gender', 'degree', 'experience', 'specialty', 'expertise', 'location')
    ordering = ('-deadline',)
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 20  # Giới hạn mỗi trang hiển thị tối đa 20 ứng viên


    fieldsets = (
        ('📌 Thông tin chung', {'fields': ('title', 'slug', 'specialty', 'expertise', 'image')}),
        ('📋 Chi tiết tuyển dụng', {'fields': ('location', 'salary', 'job_type', 'degree', 'experience', 'gender', 'level', 'quantity', 'deadline')}),
        ('📖 Nội dung mô tả', {'fields': ('benefits', 'requirements', 'description', 'rights')}),
    )




class ApplicantAdmin(admin.ModelAdmin):
    list_display = (
        "full_name", "dob", "phone", "gender", "status", "cccd", "email",
        "job_title", "city", "district", "ward", "street", "education",
        "experience", "source", "download_cv", "download_image", "applied_at"
    )
    list_per_page = 20  # Giới hạn mỗi trang hiển thị tối đa 20 ứng viên

    readonly_fields = (
        "full_name", "dob", "phone", "gender", "status", "cccd", "email",
        "about", "job_title", "city", "district", "ward", "street",
        "education", "experience", "source", "cv", "portrait", "applied_at"
    )

    search_fields = (
        "full_name", "phone", "email", "cccd", "job_title",
        "city", "district", "ward", "street"
    )

    list_filter = ("gender", "status", "education", "experience", "source", "city", "district")
    actions = ["send_interview_email"]  # Thêm action gửi mail

    def download_cv(self, obj):
        """Nút tải CV"""
        if obj.cv:
            return mark_safe(f'<a href="{obj.cv.url}" download class="button">📄 Tải CV</a>')
        return "Không có CV"
    download_cv.short_description = "Hồ sơ ứng viên"

    def download_image(self, obj):
        """Nút tải hình ảnh"""
        if obj.portrait:
            return mark_safe(f'<a href="{obj.portrait.url}" download class="button">🖼️ Tải ảnh</a>')
        return "Không có ảnh"
    download_image.short_description = "Ảnh chân dung"

    def has_add_permission(self, request):
        """Chặn tạo mới"""
        return False

    def has_change_permission(self, request, obj=None):
        """Chặn chỉnh sửa"""
        return False

    def has_delete_permission(self, request, obj=None):
        """Chặn xóa"""
        return False
    
def get_search_results(self, request, queryset, search_term):
    search_term = unidecode(search_term).lower()

    queryset = queryset.filter(
        Q(full_name__icontains=search_term) |
        Q(phone__icontains=search_term) |
        Q(email__icontains=search_term) |
        Q(cccd__icontains=search_term) |
        Q(job_title__icontains=search_term) |
        Q(city__icontains=search_term) |
        Q(district__icontains=search_term) |
        Q(ward__icontains=search_term) |
        Q(street__icontains=search_term)
    )

    return queryset, False

admin.site.register(Applicant, ApplicantAdmin)

class EmailTemplateAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": CKEditor5Widget(config_name="default")},
    }

admin.site.register(EmailTemplate, EmailTemplateAdmin)
