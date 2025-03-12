from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "gallery_album"

    def __str__(self):
        return self.title

class Image(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="images")
    file = models.ImageField(upload_to='gallery/images/')  # Không cần 'media/'
    title = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "gallery_image"

    def __str__(self):
        return self.title or f"Hình ảnh trong {self.album.title}"


class Video(models.Model):
    title = models.CharField(max_length=255)
    youtube_link = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "gallery_video"

    def embed_url(self):
        return self.youtube_link.replace("watch?v=", "embed/")

    def __str__(self):
        return self.title
    

class News(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='gallery/news_thumbnails/', blank=True, null=True)  # Ảnh đại diện
    content = CKEditor5Field("Nội dung", config_name="extends")  # CKEditor 5 cho nội dung
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title