import random
from faker import Faker
from job.models import Job, Applicant  # Thay 'job' bằng tên app của bạn
from django.utils.text import slugify
from datetime import date, timedelta

fake = Faker('vi_VN')
job_types = ['fulltime', 'parttime', 'freelance', 'intern']
specialties = ['nhi', 'san', 'tim', 'mat', 'ivhealth', 'tiemchung', 'vanphong']
expertises = ['kiemsoat', 'thuocduoc', 'vatset', 'trienkhai', 'kythuat', 'itphanmem', 'marketing']
locations = ['hanoi', 'hochiminh', 'danang', 'cantho', 'binhduong']
genders = ['any', 'male', 'female']
levels = ['manager', 'head', 'assistant', 'staff', 'intern']

for _ in range(50):
    title = fake.job()
    slug = slugify(title)
    deadline = date.today() + timedelta(days=random.randint(10, 60))
    
    job = Job.objects.create(
        title=title,
        slug=slug,
        specialty=random.choice(specialties),
        expertise=random.choice(expertises),
        deadline=deadline,
        location=random.choice(locations),
        office=fake.address(),
        salary=f"{random.randint(10, 100)} triệu/tháng",
        job_type=random.choice(job_types),
        degree=fake.sentence(),
        experience=f"{random.randint(1, 10)} năm",
        gender=random.choice(genders),
        level=random.choice(levels),
        quantity=random.randint(1, 10),
        benefits=fake.text(),
        requirements=fake.text(),
        description=fake.text(),
        rights=fake.text(),
    )
    print(f"Đã tạo công việc: {title}")
