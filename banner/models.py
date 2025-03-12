from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tiêu đề")
    image = models.ImageField(upload_to='banners/', verbose_name="Hình ảnh")
    is_active = models.BooleanField(default=True, verbose_name="Hiển thị")
    order = models.PositiveIntegerField(default=0, verbose_name="Thứ tự sắp xếp")

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
        ordering = ['order']

    def __str__(self):
        return self.title

