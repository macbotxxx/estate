from django.forms import ModelForm
from .models import UploadProperties, HomePageImages, Companyinformation, Testmonials

class UploadProperty(ModelForm):
      class Meta:
            model = UploadProperties
            fields = '__all__'
            exclude = ['slug']

class HomePageImage(ModelForm):
      class Meta:
            model = HomePageImages
            fields = '__all__'
            exclude = ['company_image']

class CompanyDetails(ModelForm):
      class Meta:
            model = Companyinformation
            fields = '__all__'
            exclude = ['company_logo_light','company_logo_dark']
            
            
class CompanyLogo(ModelForm):
      class Meta:
            model = Companyinformation
            fields = ['company_logo_light', 'company_logo_dark']
      

class CustomerReviews(ModelForm):
      class Meta:
            model = Testmonials
            fields = '__all__'