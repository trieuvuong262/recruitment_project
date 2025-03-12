# Generated by Django 5.1.2 on 2025-03-10 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Tên công việc')),
                ('specialty', models.CharField(max_length=255, verbose_name='Chuyên khoa')),
                ('expertise', models.TextField(verbose_name='Chuyên môn')),
                ('image', models.ImageField(blank=True, null=True, upload_to='jobs/', verbose_name='Hình ảnh')),
                ('deadline', models.DateField(verbose_name='Hạn nộp CV')),
                ('location', models.CharField(max_length=255, verbose_name='Vị trí làm việc')),
                ('office', models.CharField(max_length=255, verbose_name='Văn phòng làm việc')),
                ('salary', models.CharField(max_length=100, verbose_name='Thu nhập')),
                ('job_type', models.CharField(choices=[('fulltime', 'Full-time'), ('parttime', 'Part-time'), ('freelance', 'Freelance'), ('intern', 'Thực tập')], max_length=20, verbose_name='Hình thức làm việc')),
                ('degree', models.CharField(max_length=255, verbose_name='Bằng cấp yêu cầu')),
                ('experience', models.CharField(max_length=255, verbose_name='Kinh nghiệm')),
                ('gender', models.CharField(choices=[('any', 'Không yêu cầu'), ('male', 'Nam'), ('female', 'Nữ')], max_length=10, verbose_name='Giới tính yêu cầu')),
                ('level', models.CharField(max_length=255, verbose_name='Cấp bậc')),
                ('quantity', models.PositiveIntegerField(verbose_name='Số lượng tuyển dụng')),
                ('benefits', models.TextField(verbose_name='Phúc lợi')),
                ('requirements', models.TextField(verbose_name='Yêu cầu công việc')),
                ('description', models.TextField(verbose_name='Mô tả công việc')),
                ('rights', models.TextField(verbose_name='Quyền lợi')),
            ],
        ),
    ]
