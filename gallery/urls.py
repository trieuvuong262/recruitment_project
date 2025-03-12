from django.urls import path
from .views import gallery_home, album_detail, gallery_news,news_detail

urlpatterns = [
    path('', gallery_home, name='gallery'),
    path('album/<int:album_id>/', album_detail, name='album_detail'),
    path('news/', gallery_news, name='gallery_news'),
    path('news/<int:news_id>/', news_detail, name='news_detail'),  # Fix lỗi
]
