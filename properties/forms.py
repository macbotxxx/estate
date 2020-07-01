from django.forms import ModelForm
from .models import UploadProperties

class UploadProperty(ModelForm):
      class Meta:
            model = UploadProperties
            fields = '__all__'
            exclude = ['slug']