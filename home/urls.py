from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('jobs/specialty/', views.jobs_by_specialty, name='jobs_by_specialty'),
    path('jobs/expertise/', views.jobs_by_expertise, name='jobs_by_expertise'),
    path('jobs/location/', views.jobs_by_location, name='jobs_by_location'),
    path('jobs/office/', views.office_jobs, name='office_jobs'),
    path('news/', views.news, name='news'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('apply/', views.apply, name='apply'),
]
