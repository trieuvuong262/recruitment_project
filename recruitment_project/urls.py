
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),  # Thêm dòng này
    path('job/', include('job.urls')),
    path('gallery/', include('gallery.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
