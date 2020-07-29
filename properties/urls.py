from django.urls import path
from .views import ( 
      home,propertiesDetails,propertylist,properties,listingType,
      adminhome, upload, propertyListAd, propertyEdit, deleteProrperty,
      contact, aboutUs, testimonies, featured,request,contactus, companydetails,editcompanyDetails,companylogoedit
      ,companyimg ,companyQues, faq, deletefaq, aboutuss, editAbout, worker,editWorker, text, customerReviews, addingCusR,
      editCusR,deleteCusR
      )

urlpatterns = [
      path('',home, name="home"),
      path('text/',text, name="text"),
      path('cusR/',customerReviews, name="cusR"),
      path('addcusR/',addingCusR, name="addcusR"),
      path('editcusR/<pk>/',editCusR, name="editcusR"),
      path('deleteCusR/<pk>/',deleteCusR, name="deleteCusR"),
      path('sending-request/',request, name="request"),
      path('faq/',companyQues, name="faq"),
      path('worker/',worker, name="worker"),
      path('about-company/',aboutuss, name="about-company"),
      path('edit-about-company/<pk>/',editAbout, name="edit-about-company"),
      path('deletefaq/<pk>/',deletefaq, name="deletefaq"),
      path('edit_worker/<pk>/',editWorker, name="edit_worker"),
      path('questions/',faq, name="questions"),
      path('company_logo_edit/<pk>/',companylogoedit, name="company_logo_edit"),
      path('contactus/',contactus, name="contactus"),
      path('contact-us/',contact, name="contact-us"),
      path('company_details/',companydetails, name="company_details"),
      path('about/',aboutUs, name="about"),
      path('edit_image_slide/<pk>/',companyimg, name="edit_image_slide"),
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
