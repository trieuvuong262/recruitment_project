from django import forms
from .models import Album

class MultipleImageUploadForm(forms.Form):
    album = forms.ModelChoiceField(queryset=Album.objects.all(), label="Chọn Album")
