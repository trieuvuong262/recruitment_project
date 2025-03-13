from django import forms
from .models import Applicant
import requests  # Dùng để gọi API
from .models import EmailTemplate
from django.conf import settings

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'
        widgets = {
            'job_title': forms.TextInput(attrs={'placeholder': 'Tiêu đề'}),
            'full_name': forms.TextInput(attrs={'placeholder': 'Nhập họ và tên'}),
            'cccd': forms.TextInput(attrs={'placeholder': 'Nhập số CCCD/CMND'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Nhập email nhận kết quả'}),
            'about': forms.Textarea(attrs={'placeholder': 'Giới thiệu bản thân'}),
            'street': forms.TextInput(attrs={'placeholder': 'Nhập số nhà, đường'}),
            'education': forms.TextInput(attrs={'placeholder': 'Nhập học vấn'}),
            'experience': forms.TextInput(attrs={'placeholder': 'Nhập kinh nghiệm làm việc'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        city_id = cleaned_data.get("city")
        district_id = cleaned_data.get("district")
        ward_id = cleaned_data.get("ward")

        # Gọi API để lấy tên tương ứng với ID
        response = requests.get("https://provinces.open-api.vn/api/?depth=3")
        if response.status_code == 200:
            data = response.json()

            # Tìm tên thành phố theo ID
            city_name = next((p['name'] for p in data if str(p['code']) == str(city_id)), None)
            cleaned_data["city"] = city_name

            # Tìm quận/huyện
            for p in data:
                district = next((d for d in p['districts'] if str(d['code']) == str(district_id)), None)
                if district:
                    cleaned_data["district"] = district['name']
                    # Tìm xã/phường
                    ward = next((w for w in district['wards'] if str(w['code']) == str(ward_id)), None)
                    if ward:
                        cleaned_data["ward"] = ward['name']
                    break

        return cleaned_data



class EmailTemplateForm(forms.Form):
    sender_email = forms.ChoiceField(choices=[], label="Email gửi")
    email_template = forms.ModelChoiceField(queryset=EmailTemplate.objects.all(), label="Mẫu email")

    def __init__(self, *args, email_choices=None, **kwargs):
        super().__init__(*args, **kwargs)
        if email_choices:
            self.fields["sender_email"].choices = email_choices