from django.shortcuts import render
from django.urls import path
from .views import job_list, job_detail,job_apply
from .views import send_email

urlpatterns = [
    path('<slug:slug>/', job_detail, name='job_detail'),  # Thêm URL cho chi tiết công việc
    path('', job_list, name='job_list'),  # URL danh sách công việc
    path('<slug:slug>/apply/', job_apply, name='job_apply'),
    path('apply/success/', lambda request: render(request, 'job/apply_success.html'), name='apply_success'),
    path("send-email/<int:applicant_id>/", send_email, name="send_email"),

]
