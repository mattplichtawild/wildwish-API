from django import forms
from .models import Image
from .models import Wish


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('upload',)