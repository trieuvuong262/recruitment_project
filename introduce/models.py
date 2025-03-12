from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class CompanyIntroduction(models.Model):
    image = models.ImageField(upload_to='company/', verbose_name="Hình ảnh")
    description = CKEditor5Field('Mô tả', config_name='default')
    
    def __str__(self):
        return "Giới thiệu công ty"

    class Meta:
        verbose_name = "Giới thiệu công ty"
        verbose_name_plural = "Giới thiệu công ty"

