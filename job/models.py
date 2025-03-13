from django.test import TestCase

# Create your tests here.
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field  # Import CKEditor5
from django.utils.text import slugify
from django.utils import timezone  # Import timezone

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Freelance', 'Freelance'),
        ('Thực tập', 'Thực tập'),
    ]

    GENDER_CHOICES = [
        ('Không yêu cầu', 'Không yêu cầu'),
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ'),
    ]

    SPECIALTY_CHOICES = [
        ('Nhi Khoa 315', 'Nhi Khoa 315'),
        ('Sản Phụ Khoa 315', 'Sản Phụ Khoa 315'),
        ('Tim Mạch Tiểu Đường 315', 'Tim Mạch Tiểu Đường 315'),
        ('Mắt 315', 'Mắt 315'),
        ('Đa Khoa Quốc Tế IVYHEALTH', 'Đa Khoa Quốc Tế IVYHEALTH'),
        ('Tiêm Chủng', 'Tiêm Chủng'),
        ('Văn Phòng', 'Văn Phòng'),
    ]

    EXPERTISE_CHOICES = [
        ('Kiểm soát nội bộ', 'Kiểm soát nội bộ'),
        ('Thu mua Dược', 'Thu mua Dược'),
        ('Thu mua Vật tư - Set up', 'Thu mua Vật tư - Set up'),
        ('Triển Khai - Hồ sơ', 'Triển Khai - Hồ sơ'),
        ('Kỹ thuật', 'Kỹ thuật'),
        ('IT - Phần mềm', 'IT - Phần mềm'),
        ('Kỹ Thuật viên', 'Kỹ Thuật viên'),
        ('Kế toán', 'Kế toán'),
        ('Marketing', 'Marketing'),
        ('Nhân sự', 'Nhân sự'),
        ('Quản lý vận hành Lễ Tân', 'Quản lý vận hành Lễ Tân'),
        ('Quản lý vận hành Dược', 'Quản lý vận hành Dược'),
        ('Quản lý vận hành Tiêm chủng', 'Quản lý vận hành Tiêm chủng'),
        ('Kho tổng', 'Kho tổng'),
        ('Hành chánh', 'Hành chánh'),
        ('Tài chính', 'Tài chính'),
        ('Quản lý dự án', 'Quản lý dự án'),
        ('Trợ lý BGĐ', 'Trợ lý BGĐ'),
        ('Quản lý chất lượng', 'Quản lý chất lượng'),
        ('Bác sĩ', 'Bác sĩ'),
        ('Điều dưỡng', 'Điều dưỡng'),
        ('Dược sĩ', 'Dược sĩ'),
        ('Lễ tân', 'Lễ tân'),
        ('Bảo vệ', 'Bảo vệ'),
    ]

    LEVEL_CHOICES = [
        ('manager', 'Quản Lý'),
        ('head', 'Trưởng Phòng'),
        ('assistant', 'Trợ Lý'),
        ('staff', 'Nhân Viên'),
        ('intern', 'Công Tác Viên'),
    ]

    LOCATION_CHOICES = [
    ('Hà Nội', 'Hà Nội'), ('Hồ Chí Minh', 'Hồ Chí Minh'), ('An Giang', 'An Giang'), ('Bà Rịa - Vũng Tàu', 'Bà Rịa - Vũng Tàu'),
    ('Bắc Giang', 'Bắc Giang'), ('Bắc Kạn', 'Bắc Kạn'), ('Bạc Liêu', 'Bạc Liêu'), ('Bắc Ninh', 'Bắc Ninh'),
    ('Bến Tre', 'Bến Tre'), ('Bình Dương', 'Bình Dương'), ('Bình Định', 'Bình Định'), ('Bình Phước', 'Bình Phước'),
    ('Bình Thuận', 'Bình Thuận'), ('Cà Mau', 'Cà Mau'), ('Cần Thơ', 'Cần Thơ'), ('Cao Bằng', 'Cao Bằng'),
    ('Đà Nẵng', 'Đà Nẵng'), ('Đắk Lắk', 'Đắk Lắk'), ('Đắk Nông', 'Đắk Nông'), ('Điện Biên', 'Điện Biên'),
    ('Đồng Nai', 'Đồng Nai'), ('Đồng Tháp', 'Đồng Tháp'), ('Gia Lai', 'Gia Lai'), ('Hà Giang', 'Hà Giang'),
    ('Hà Nam', 'Hà Nam'), ('Hà Tĩnh', 'Hà Tĩnh'), ('Hải Dương', 'Hải Dương'), ('Hải Phòng', 'Hải Phòng'),
    ('Hậu Giang', 'Hậu Giang'), ('Hòa Bình', 'Hòa Bình'), ('Hưng Yên', 'Hưng Yên'), ('Khánh Hòa', 'Khánh Hòa'),
    ('Kiên Giang', 'Kiên Giang'), ('Kon Tum', 'Kon Tum'), ('Lai Châu', 'Lai Châu'), ('Lâm Đồng', 'Lâm Đồng'),
    ('Lạng Sơn', 'Lạng Sơn'), ('Lào Cai', 'Lào Cai'), ('Long An', 'Long An'), ('Nam Định', 'Nam Định'),
    ('Nghệ An', 'Nghệ An'), ('Ninh Bình', 'Ninh Bình'), ('Ninh Thuận', 'Ninh Thuận'), ('Phú Thọ', 'Phú Thọ'),
    ('Phú Yên', 'Phú Yên'), ('Quảng Bình', 'Quảng Bình'), ('Quảng Nam', 'Quảng Nam'), ('Quảng Ngãi', 'Quảng Ngãi'),
    ('Quảng Ninh', 'Quảng Ninh'), ('Quảng Trị', 'Quảng Trị'), ('Sóc Trăng', 'Sóc Trăng'), ('Sơn La', 'Sơn La'),
    ('Tây Ninh', 'Tây Ninh'), ('Thái Bình', 'Thái Bình'), ('Thái Nguyên', 'Thái Nguyên'), ('Thanh Hóa', 'Thanh Hóa'),
    ('Thừa Thiên Huế', 'Thừa Thiên Huế'), ('Tiền Giang', 'Tiền Giang'), ('Trà Vinh', 'Trà Vinh'), ('Tuyên Quang', 'Tuyên Quang'),
    ('Vĩnh Long', 'Vĩnh Long'), ('Vĩnh Phúc', 'Vĩnh Phúc'), ('Yên Bái', 'Yên Bái')
]
    
    slug = models.SlugField(unique=True, blank=True,verbose_name="Tên viết tắt")
    title = models.CharField(max_length=255, verbose_name="Tên công việc")
    specialty = models.CharField(max_length=255, choices=SPECIALTY_CHOICES, verbose_name="Chuyên khoa")
    expertise = models.CharField(max_length=255, choices=EXPERTISE_CHOICES, verbose_name="Chuyên môn")
    image = models.ImageField(upload_to='jobs/', verbose_name="Hình ảnh", blank=True, null=True)
    deadline = models.DateField(verbose_name="Hạn nộp CV")
    location = models.CharField(max_length=255, choices=LOCATION_CHOICES,verbose_name="Vị trí làm việc")
    office = models.CharField(max_length=255, verbose_name="Văn phòng làm việc")
    salary = models.CharField(max_length=255, verbose_name="Thu nhập")
    job_type = models.CharField(max_length=255, choices=JOB_TYPE_CHOICES, verbose_name="Hình thức làm việc")
    degree = models.CharField(max_length=255, verbose_name="Bằng cấp yêu cầu")
    experience = models.CharField(max_length=255, verbose_name="Kinh nghiệm")
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, verbose_name="Giới tính yêu cầu")
    level = models.CharField(max_length=255, choices=LEVEL_CHOICES, verbose_name="Cấp bậc")
    quantity = models.PositiveIntegerField(verbose_name="Số lượng tuyển dụng")
    created_at = models.DateTimeField(default=timezone.now)  # Lấy ngày thực tế

    # Sử dụng CKEditor5 cho các trường dài
    benefits = CKEditor5Field(verbose_name="Phúc lợi", config_name='extends')
    requirements = CKEditor5Field(verbose_name="Yêu cầu công việc", config_name='extends')
    description = CKEditor5Field(verbose_name="Mô tả công việc", config_name='extends')
    rights = CKEditor5Field(verbose_name="Quyền lợi", config_name='extends')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Tạo slug tự động từ title
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Danh sách công việc"

    def __str__(self):
        return self.title
    

class Applicant(models.Model):
    full_name = models.CharField("Họ và tên của ứng viên", max_length=255)
    dob = models.DateField("Ngày sinh")
    phone = models.CharField("Số điện thoại", max_length=15)
    gender = models.CharField("Giới tính", max_length=10, choices=[('Nam', 'Nam'), ('Nữ', 'Nữ'), ('Khác', 'Khác')])
    status = models.CharField("Tình trạng hôn nhân", max_length=20, choices=[('Độc thân', 'Độc thân'), ('Đã kết hôn', 'Đã kết hôn')])
    cccd = models.CharField("CCCD/CMND", max_length=12, blank=True, null=True)
    email = models.EmailField("Email", blank=True, null=True)
    about = models.TextField("Giới thiệu bản thân", blank=True, null=True)
    job_title = models.CharField("Vị trí ứng tuyển", max_length=255, blank=True, null=True)  # Thêm trường này

    # Trường lấy từ API
    city = models.CharField("Tỉnh/Thành phố", max_length=255, blank=True, null=True)
    district = models.CharField("Quận/Huyện", max_length=255, blank=True, null=True)
    ward = models.CharField("Xã/Phường", max_length=255, blank=True, null=True)
    street = models.CharField("Địa chỉ cụ thể", max_length=255, blank=True, null=True)

    education = models.CharField("Trình độ học vấn", max_length=255)
    experience = models.CharField("Kinh nghiệm", max_length=255)
    source = models.CharField("Nguồn ứng tuyển", max_length=50, choices=[
        ('Facebook', 'Facebook'),
        ('Website', 'Website'),
        ('Người quen giới thiệu', 'Người quen giới thiệu'),
        ('Khác', 'Khác')
    ])
    cv = models.FileField("Hồ sơ ứng viên", upload_to='uploads/cv/', blank=True, null=True)
    portrait = models.ImageField("Ảnh chân dung", upload_to='uploads/portrait/', blank=True, null=True)
    applied_at = models.DateTimeField("Ngày ứng tuyển", auto_now_add=True)

    class Meta:
        verbose_name = "Ứng viên"
        verbose_name_plural = "Danh sách ứng viên"

    def __str__(self):
        return self.full_name

class EmailTemplate(models.Model):
    subject = models.CharField(
        max_length=255,
        default="Xác nhận ứng tuyển: {job_title}",
        verbose_name="Tiêu đề Email"
    )
    body = CKEditor5Field(
        verbose_name="Nội dung Email",
        config_name="default",
        default=(
            "Bạn có thể sử dụng các biến sau trong email:<br>"
            "- Họ tên: {full_name}<br>"
            "- Ngày sinh: {dob}<br>"
            "- Số điện thoại: {phone}<br>"
            "- Email: {email}<br>"
            "- Địa chỉ: {street}, {ward}, {district}, {city}<br>"
            "- Học vấn: {education}<br>"
            "- Kinh nghiệm: {experience}<br>"
            "- Vị trí: {job_title}"
        )
    )
    signature_url = models.URLField(
        null=True,
        blank=True,
        verbose_name="URL Chữ ký (Google Drive link)"
    )

    class Meta:
        verbose_name_plural = "Mẫu Email"

    def __str__(self):
        return self.subject


