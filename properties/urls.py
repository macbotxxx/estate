from django.urls import path
from .views import ( 
      home,propertiesDetails,propertylist,properties,listingType,
      adminhome, upload, propertyListAd, propertyEdit, deleteProrperty,
      contact, aboutUs, testimonies, featured,request,contactus, companydetails,editcompanyDetails, companylogo,companylogoedit
      )

urlpatterns = [
      path('',home, name="home"),
      path('sending-request/',request, name="request"),
      path('company_logo/',companylogo, name="company_logo"),
      path('company_logo_edit/<pk>/',companylogoedit, name="company_logo_edit"),
      path('contactus/',contactus, name="contactus"),
      path('contact-us/',contact, name="contact-us"),
      path('company_details/',companydetails, name="company_details"),
      path('about/',aboutUs, name="about"),
      path('customers-review/',testimonies, name="customers-review"),
      path('featured-properties/',featured, name="featured-properties"),
      path('property_details/<slug>/',propertiesDetails, name="property_details"),
      path('property_search/',propertylist, name="property_search"),
      path('property_list/',properties, name="property_list"),
      path('property/<tag>/',listingType, name="property"),
      path('managerdesk/',adminhome, name="managerdesk"),
      path('upload/',upload, name="upload"),
      path('property-list/',propertyListAd, name="property-list"),
      path('property-edit/<pk>/',propertyEdit, name="property-edit"),
      path('company-edit/<pk>/',editcompanyDetails, name="company-edit"),
      path('delete-property/<pk>/',deleteProrperty, name="delete-property"),

]
