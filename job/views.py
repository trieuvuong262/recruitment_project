import os
from django.shortcuts import render, get_object_or_404,redirect
from .models import EmailTemplate, Job, Applicant
from .forms import ApplicantForm
from django.core.paginator import Paginator
from django.db.models import Q
from unidecode import unidecode 
from django.conf import settings
from django.core.mail import EmailMultiAlternatives, get_connection
import mimetypes
import base64
from django.http import HttpRequest
from .forms import EmailTemplateForm
from django.contrib import messages


def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    related_jobs = Job.objects.filter(specialty=job.specialty).exclude(id=job.id)[:3]

    return render(request, "job/job_detail.html", {"job": job,"related_jobs": related_jobs})

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


def job_apply(request: HttpRequest, slug):
    job = get_object_or_404(Job, slug=slug)

    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job_title = job.title
            application.save()

            recipient_email = application.email  # Email của ứng viên

            # Lấy mẫu email từ database
            email_template = EmailTemplate.objects.first()
            if email_template:
                subject = email_template.subject.format(job_title=job.title)
                html_content = email_template.body.format(
                    job_title=job.title,
                    full_name=application.full_name,
                    dob=application.dob,
                    phone=application.phone,
                    email=application.email if application.email else 'Không cung cấp',
                    street=application.street,
                    ward=application.ward,
                    district=application.district,
                    city=application.city,
                    education=application.education,
                    experience=application.experience,
                    cv=f'<a href="{application.cv.url}">Tải CV</a>' if application.cv else "Chưa tải lên"
                )

                # Xử lý ảnh CKEditor trong nội dung email
                for img_tag in ['<img src="', "<img src='"]:
                    while img_tag in html_content:
                        start_index = html_content.find(img_tag) + len(img_tag)
                        end_index = html_content.find('"', start_index) if img_tag == '<img src="' else html_content.find("'", start_index)
                        img_path = html_content[start_index:end_index]

                        if img_path.startswith('/media/'):  # Kiểm tra nếu ảnh thuộc media
                            img_full_path = os.path.join(settings.MEDIA_ROOT, img_path.replace('/media/', ''))

                            try:
                                with open(img_full_path, "rb") as img_file:
                                    img_data = base64.b64encode(img_file.read()).decode('utf-8')
                                    mime_type, _ = mimetypes.guess_type(img_path)
                                    new_src = f"data:{mime_type};base64,{img_data}"
                                    html_content = html_content.replace(img_path, new_src)
                            except FileNotFoundError:
                                print(f"LỖI: Không tìm thấy ảnh {img_full_path}")
                            except Exception as e:
                                print(f"LỖI khi xử lý ảnh: {e}")

                # Gửi email HTML
                email = EmailMultiAlternatives(
                    subject=subject,
                    body="Vui lòng xem email dưới dạng HTML.",
                    from_email=settings.EMAIL_HOST_USER,
                    to=[recipient_email]
                )
                email.attach_alternative(html_content, "text/html")
                email.send()  # Gửi email

            return redirect('apply_success')

    else:
        form = ApplicantForm()

    return render(request, 'job/apply.html', {'job': job, 'form': form})


def send_email(request, applicant_id):
    applicant = get_object_or_404(Applicant, id=applicant_id)

    # Lấy danh sách email từ settings
    email_choices = [(account["email"], account["name"]) for account in settings.EMAIL_ACCOUNTS]

    if request.method == "POST":
        form = EmailTemplateForm(request.POST, email_choices=email_choices)
        if form.is_valid():
            sender_email = form.cleaned_data["sender_email"]
            email_template = form.cleaned_data["email_template"]

            # Lấy thông tin tài khoản email
            selected_account = next((acc for acc in settings.EMAIL_ACCOUNTS if acc["email"] == sender_email), None)
            
            if not selected_account:
                messages.error(request, "Email không hợp lệ.")
                return redirect("admin:job_applicant_changelist")

            email_host_user = selected_account["email"]
            email_host_password = selected_account.get("password")

            if not email_host_password:
                messages.error(request, "Không tìm thấy mật khẩu email. Vui lòng cập nhật settings.")
                return redirect("admin:job_applicant_changelist")

            # Kiểm tra và format nội dung email
            context = {
                "full_name": getattr(applicant, "full_name", "Ứng viên"),
                "dob": getattr(applicant, "dob", "Không có"),
                "phone": getattr(applicant, "phone", "Không có"),
                "email": getattr(applicant, "email", "Không có"),
                "street": getattr(applicant, "street", ""),
                "ward": getattr(applicant, "ward", ""),
                "district": getattr(applicant, "district", ""),
                "city": getattr(applicant, "city", ""),
                "education": getattr(applicant, "education", "Không có"),
                "experience": getattr(applicant, "experience", "Không có"),
                "job_title": getattr(applicant, "job_title", "Vị trí chưa xác định"),
            }

            try:
                subject = email_template.subject.format(**context)
                html_content = email_template.body.format(**context)
            except KeyError as e:
                messages.error(request, f"Thiếu dữ liệu cho biến: {str(e)}")
                return redirect("admin:job_applicant_changelist")

            # Gửi email
            with get_connection(username=email_host_user, password=email_host_password) as connection:
                email = EmailMultiAlternatives(
                    subject=subject,
                    body="Vui lòng xem email dưới dạng HTML.",
                    from_email=email_host_user,
                    to=[applicant.email],
                    connection=connection
                )
                email.attach_alternative(html_content, "text/html")
                email.send()

            # Cập nhật trạng thái email_sent
            applicant.email_sent = True
            applicant.save()

            messages.success(request, f"Email đã gửi tới {applicant.full_name}.")
            return redirect("admin:job_applicant_changelist")
    
    else:
        form = EmailTemplateForm(email_choices=email_choices)

    return render(request, "admin/send_email.html", {"form": form, "applicant": applicant})
