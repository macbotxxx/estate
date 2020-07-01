import django_filters
from django_filters import CharFilter
from .models import UploadProperties


class PropertyFilter(django_filters.FilterSet):
      property_title = CharFilter(field_name = 'property_title', lookup_expr = 'icontains')
      class Meta:
            model = UploadProperties
            fields = ['property_title','listing_type','property_type','bedrooms','bathrooms','commission','payment_condition','state']
