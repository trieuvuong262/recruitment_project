from django.shortcuts import render, get_object_or_404,redirect
from .models import Job, Applicant
from .forms import ApplicantForm
from django.core.paginator import Paginator
from django.db.models import Q
from unidecode import unidecode 

def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    return render(request, "job/job_detail.html", {"job": job})

def job_list(request):
    jobs = Job.objects.all()

    # Lọc theo các tiêu chí
    job_type = request.GET.get('job_type')
    specialty = request.GET.get('specialty')
    expertise = request.GET.get('expertise')
    level = request.GET.get('level')
    location = request.GET.get('location')
    salary = request.GET.get('salary')
    experience = request.GET.get('experience')

    search_query = request.GET.get('search_query', '').strip()
    if search_query:
            # Chuyển đổi chuỗi tìm kiếm thành không dấu và viết thường
        normalized_query = unidecode(search_query).lower()

        # Lọc công việc dựa trên tiêu đề đã chuyển thành không dấu
        jobs = jobs.filter(
            Q(title__icontains=search_query) |  # Tìm kiếm có dấu
            Q(title__icontains=normalized_query)  # Tìm kiếm không dấu
        )
    # Xử lý bộ lọc
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    if specialty:
        jobs = jobs.filter(specialty=specialty)
    if expertise:
        jobs = jobs.filter(expertise=expertise)
    if level:
        jobs = jobs.filter(level=level)
    if location:
        jobs = jobs.filter(location=location)
    if salary:
        jobs = jobs.filter(salary=salary)
    if experience:
        jobs = jobs.filter(experience=experience)
  # Xử lý phân trang
    paginator = Paginator(jobs, 6)  # 10 công việc mỗi trang
    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)  # Lấy trang hiện tại


    job_types = sorted(Job.objects.values_list('job_type', flat=True).distinct())
    specialties = sorted(Job.objects.values_list('specialty', flat=True).distinct())
    expertises = sorted(Job.objects.values_list('expertise', flat=True).distinct())
    locations = sorted(Job.objects.values_list('location', flat=True).distinct())
    salaries = sorted(Job.objects.values_list('salary', flat=True).distinct())
    experiences = sorted(Job.objects.values_list('experience', flat=True).distinct())

    # Chuyển đổi giá trị thành tên đầy đủ (từ model choices)
    job_type_choices = dict(Job.JOB_TYPE_CHOICES)  # Giả sử bạn có JOB_TYPE_CHOICES trong model
    job_type_display = {key: job_type_choices.get(key) for key in job_types}

    context = {
        'jobs': jobs,
        'job_types': job_types,
        'specialties': specialties,
        'expertises': expertises,
        'levels': level,
        'locations': locations,
        'salaries': salaries,
        'experiences': experiences,
        'job_type_display': job_type_display,
        'search_query': search_query,  # Để hiển thị lại giá trị đã nhập

    }
    return render(request, 'job/job_list.html', context)


def job_apply(request, slug):
    job = Job.objects.get(slug=slug)

    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('apply_success')  
    else:
        form = ApplicantForm()

    return render(request, 'job/apply.html', {'job': job, 'form': form})

