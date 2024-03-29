from django.forms import ModelForm, Textarea, TextInput, Select,ClearableFileInput
from django import forms
from .models import UploadProperties, HomePageImages, Companyinformation, Testmonials, Workers, Partners, About, Fqa
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin


class UploadPropertyi(ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = UploadProperties
        fields = '__all__'
        exclude = ['slug']
        widgets = {
            'property_title': TextInput(attrs={'placeholder': 'Property Title is needed '}),
            'payment_condition': Select(attrs={'class': 'form-control'}),
            'commission': Select(attrs={'class': 'form-control'}),
            'listing_type': Select(attrs={'class': 'form-control'}),
            'tag': Select(attrs={'class': 'form-control'}),
            'property_type': Select(attrs={'class': 'form-control'}),
            'bedrooms': Select(attrs={'class': 'form-control'}),
            'bathrooms': Select(attrs={'class': 'form-control'}),
            'toilet': Select(attrs={'class': 'form-control'}),
            'garage': Select(attrs={'class': 'form-control'}),
            'property_main_image': ClearableFileInput(attrs={'id': 'imgInp'}),
            'property_image2': ClearableFileInput(attrs={'id': 'imgInp'}),
            'state': Select(attrs={'class': 'form-control'}),
            'security': Select(attrs={'class': 'form-control'}),

        }


class HomePageImage(ModelForm):
    class Meta:
        model = HomePageImages
        fields = '__all__'
        exclude = ['company_image']


class CompanyDetails(ModelForm):
    class Meta:
        model = Companyinformation
        fields = '__all__'
        exclude = ['company_logo_light', 'company_logo_dark']


class CompanyLogo(ModelForm):
    class Meta:
        model = Companyinformation
        fields = ['company_logo_light', 'company_logo_dark']


class CustomerReviews(ModelForm):
    client_comment = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Testmonials
        fields = '__all__'
        widgets = {
            'client_image': ClearableFileInput(attrs={'id': 'imgInp'}),
        }


class WorkersDetails(ModelForm):
    class Meta:
        model = Workers
        fields = '__all__'
        widgets = {
            'staff_image': ClearableFileInput(attrs={'id': 'imgInp'}),
        }

class PartnerLogo(ModelForm):
    class Meta:
        model = Partners
        fields = '__all__'


class QuestionAnswer(ModelForm):
    class Meta:
        model = Fqa
        fields = '__all__'


class CompanyAbout(ModelForm):
    about = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = About
        fields = '__all__'
        widgets = {
        'company_image':  ClearableFileInput(attrs={'id': 'imgInp'}),
        }
