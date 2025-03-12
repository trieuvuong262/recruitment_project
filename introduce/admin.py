from django.contrib import admin
from .models import CompanyIntroduction

@admin.register(CompanyIntroduction)
class CompanyIntroductionAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']
    
    def has_add_permission(self, request):
        return not CompanyIntroduction.objects.exists()
    

