from django.shortcuts import render
from banner.models import Banner
from introduce.views import get_introduction
from job.models import Job
from gallery.models import Album,Video,News



def home(request):
    latest_jobs = Job.objects.order_by('-created_at')[:6]  # Lấy 6 công việc mới nhất
    videos = Video.objects.all() 
    banners = Banner.objects.all() 
    company_intro = get_introduction()
    albums = Album.objects.all()
    news_list = News.objects.all().order_by('-created_at')  # Truyền danh sách tin tức

    return render(request, 'home/home.html', { 'news_list': news_list,'videos': videos,'albums': albums,'latest_jobs': latest_jobs,'company_intro': company_intro,'banners': banners})

def about(request):
    return render(request, 'home/about.html')


def jobs_by_specialty(request):
    return render(request, 'home/jobs_specialty.html')

def jobs_by_expertise(request):
    return render(request, 'home/jobs_expertise.html')

def jobs_by_location(request):
    return render(request, 'home/jobs_location.html')

def office_jobs(request):
    return render(request, 'home/jobs_office.html')

def news(request):
    return render(request, 'home/news.html')

def gallery(request):
    return render(request, 'home/gallery.html')

def contact(request):
    return render(request, 'home/contact.html')

def apply(request):
    return render(request, 'home/apply.html')


def job_home_filter_section(request):
    specialties = Job.objects.values_list('specialty', flat=True).distinct()
    locations = Job.objects.values_list('location', flat=True).distinct()
    levels = Job.objects.values_list('level', flat=True).distinct()

    context = {
        'specialties': specialties,
        'locations': locations,
        'levels': levels,
    }

    return render(request, 'home/home.html', context)

