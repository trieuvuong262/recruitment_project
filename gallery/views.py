from django.shortcuts import render,get_object_or_404
from .models import Album, Video, News

def gallery_home(request):
    albums = Album.objects.all()
    videos = Video.objects.all()
    news = News.objects.all()

    for video in videos:
        video.youtube_link = video.youtube_link.replace("watch?v=", "embed/")
    return render(request, 'gallery/gallery.html', {'albums': albums, 'videos': videos})

def album_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    return render(request, 'gallery/album_detail.html', {'album': album})

def gallery_news(request):
    news_list = News.objects.all().order_by('-created_at')
    return render(request, 'gallery/gallery_news.html', {'news_list': news_list})

def news_detail(request, news_id):  # Hàm xử lý chi tiết tin tức
    news = get_object_or_404(News, id=news_id)
    return render(request, 'gallery/news_detail.html', {'news': news})