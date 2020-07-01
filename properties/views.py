from django.shortcuts import render, get_object_or_404, redirect
from .models import UploadProperties, Tag, Newsletters, HomePageImages, Testmonials,  Partners, Companyinformation, Workers
from .filters import PropertyFilter
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UploadProperty
from django.contrib import messages
from django.core.paginator import Paginator


def request(request):
      if request.method == "POST":
            email = request.POST['emailx']
            message = request.POST['messagex']
            send_mail(
                  'Inquery From A Customer  ',
                        message,
                        email,
                        [settings.EMAIL_HOST_USER],
                        fail_silently=False,
                  )
            return redirect('/')

      return render(request,"main/request.htlm",{})


def contactus(request):
      if request.method == "POST":
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            send_mail(
                        subject,
                        message,
                        email,
                        [settings.EMAIL_HOST_USER],
                        fail_silently=False,
                  )
            
            send_mail(
                        'welcome to roverestate',
                        'you will hear from us soon as possible',
                        'assanamamichael@gmail.com',
                        [email],
                        fail_silently=False,
                  )
            return redirect('/')

      return render(request,"main/contactus.html",{})


def home(request):
      companydetails = Companyinformation.objects.all()
      staff = Workers.objects.all()
      recent = UploadProperties.objects.all().order_by('-time_uploaded')[:6]
      slideImages = HomePageImages.objects.all()
      recentx = UploadProperties.objects.all().order_by('-time_uploaded')[:3]
      featured = UploadProperties.objects.filter(tag='featured').order_by('-time_uploaded')[:6]
      popular = UploadProperties.objects.filter(tag='popular').order_by('-time_uploaded')[:6]
      search = UploadProperties.objects.all()
      testimonies = Testmonials.objects.all()
      partner = Partners.objects.all()
      myfilter = PropertyFilter(request.GET,queryset=search)
      search = myfilter.qs 
      list = Tag.objects.all()
      

      if request.method == "POST":
            email = request.POST['email']
            if Newsletters.objects.filter(email=email).exists():
                  emailuser = email
                  subject = "ROVERESTATE YOU ARE ALREADY A MEMBER"
                  from_email = settings.EMAIL_HOST_USER
                  to_email = emailuser
                  with open(settings.BASE_DIR + "/templates/emails/alreadyexist.txt") as f:
                        signup_message = f.read()
                  message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email,to=[to_email])
                  html_template = get_template("emails/alreadyexist.html").render()
                  message.attach_alternative(html_template, "text/html")
                  message.send()
            else:
                  new_signup = Newsletters()
                  new_signup.email = email
                  new_signup.save()
                  emailuser = email
                  subject = "ROVERESTATE THANKS FOR SUBCRIBING FOR UPDATES"
                  from_email = settings.EMAIL_HOST_USER
                  to_email = emailuser
                  with open(settings.BASE_DIR + "/templates/emails/newsletter.txt") as f:
                        signup_message = f.read()
                  message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email,to=[to_email])
                  html_template = get_template("emails/newsletter.html").render()
                  message.attach_alternative(html_template, "text/html")
                  message.send()

      
           
      context = {
            'staff':staff,
            'partner':partner,
            'testimonies':testimonies,
            'slideImages':slideImages,
            'recentx':recentx,
            'list': list,
            'popular':popular,
            'featured':featured,
            'myfilter':myfilter,
            'recent': recent,
            'companydetails':companydetails,
      }
      return render(request,'main/index.html',context)

def propertiesDetails(request, slug):
      recent = UploadProperties.objects.all().order_by('-time_uploaded')[:6]
      companydetails = Companyinformation.objects.all()
      details = get_object_or_404(UploadProperties,slug=slug)
      search = UploadProperties.objects.all()
      sale = UploadProperties.objects.filter(listing_type='sale').order_by('-time_uploaded')[:4]
      rent = UploadProperties.objects.filter(listing_type='rent').order_by('-time_uploaded')[:4]
      myfilter = PropertyFilter(request.GET, queryset=search)
      search = myfilter.qs
      tagx = Tag.objects.all()
      context = {
            'recent':recent,
            'companydetails':companydetails,
            'tagx':tagx,
            'sale': sale,
            'rent': rent,
            'myfilter':myfilter,
            'details': details
      }
      return render(request,'main/property_details.html',context)


def properties(request):
      recent = UploadProperties.objects.all().order_by('-time_uploaded')[:6]
      companydetails = Companyinformation.objects.all()
      allproperties = UploadProperties.objects.all().order_by('-time_uploaded')
      search = UploadProperties.objects.all()
      paginator = Paginator(allproperties, 9) # Show 25 contacts per page.
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
      myfilter = PropertyFilter(request.GET, queryset=search)
      search = myfilter.qs
      list = Tag.objects.all()
      # count = UploadProperties.objects.all().count()
      context = {
            'recent':recent,
            'companydetails':companydetails,
            'page_obj': page_obj,
            'myfilter':myfilter,
            # 'count':count,
            'allproperties': allproperties,
            'list': list
      }
      return render(request,'main/properties_listing.html', context)


def propertylist(request):
      recent = UploadProperties.objects.all().order_by('-time_uploaded')[:6]
      companydetails = Companyinformation.objects.all()
      list = Tag.objects.all()
      search = UploadProperties.objects.all()
      myfilter = PropertyFilter(request.GET, queryset=search)
      search = myfilter.qs
      count = myfilter.qs.count()
      tagx = Tag.objects.all()
      context = {
            'recent':recent,
            'companydetails':companydetails,
            'tagx':tagx,
            'myfilter':myfilter,
            'search':search,
            'count':count,
            'list':list
      }
      return render(request,'main/properties_search.html',context)


def listingType(request, tag):
      recent = UploadProperties.objects.all().order_by('-time_uploaded')[:6]
      companydetails = Companyinformation.objects.all()
      allproperties = UploadProperties.objects.filter(listing_type=tag)
      tagx = Tag.objects.all()
      search = UploadProperties.objects.all()
      myfilter = PropertyFilter(request.GET, queryset=search)
      search = myfilter.qs
      count = allproperties.count()
      email = Newsletters.objects.all()
      paginator = Paginator(allproperties, 9) # Show 25 contacts per page.
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
      context = {
            'recent':recent,
            'companydetails':companydetails,
            'page_obj':page_obj,
            'email':email,
            'allproperties': allproperties,
            'tagx':tagx,
            'myfilter':myfilter,
            'count':count,
      }

      return render(request,'main/property.html',context)

def contact(request):
      recent = UploadProperties.objects.all().order_by('-time_uploaded')[:6]
      companydetails = Companyinformation.objects.all()
      list = Tag.objects.all()
      context = {
            'recent':recent,
            'companydetails':companydetails,
            'list':list,

      }
      return render(request,"main/contacts.html",context)

def aboutUs(request):
      recent = UploadProperties.objects.all().order_by('-time_uploaded')[:6]
      companydetails = Companyinformation.objects.all()
      list = Tag.objects.all()
      context = {
            'recent':recent,
            'companydetails':companydetails,
            'list':list

      }
      return render(request,"main/about_us.html",context)

def testimonies(request):
      recent = UploadProperties.objects.all().order_by('-time_uploaded')[:6]
      companydetails = Companyinformation.objects.all()
      testimonies = Testmonials.objects.all()
      search = UploadProperties.objects.all()
      myfilter = PropertyFilter(request.GET, queryset=search)
      search = myfilter.qs
      list = Tag.objects.all()
      context = {
            'recent':recent,
            'companydetails':companydetails,
            'testimonies':testimonies,
            'myfilter':myfilter,
            'list':list

      }
      return render(request,"main/reviews.html",context)

def featured(request):
      recent = UploadProperties.objects.all().order_by('-time_uploaded')[:6]
      companydetails = Companyinformation.objects.all()
      allproperties = UploadProperties.objects.filter(tag='featured')
      count = allproperties.count()
      paginator = Paginator(allproperties, 9) # Show 25 contacts per page.
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
      list = Tag.objects.all()
      search = UploadProperties.objects.all()
      myfilter = PropertyFilter(request.GET, queryset=search)
      search = myfilter.qs
      context = {
            'recent':recent,
            'companydetails':companydetails,
            'page_obj':page_obj,
            'allproperties': allproperties,
            'myfilter':myfilter,
            'list':list,
            'count':count,
      }
      return render(request,"main/featured.html",context)


# ===============================================================================================================================================================
# ===========================================================ADMIN DASHBOARD FUNCTIONS ==========================================================================
# ***************************************************************************************************************************************************************

@login_required()
def adminhome(request):
      property_count = UploadProperties.objects.count()
      property_feature =  UploadProperties.objects.filter(tag='featured').count()
      subcribers = Newsletters.objects.count()
      xx = request.user
      context = {
            'subcribers': subcribers,
            'xx': xx,
            'property_feature':property_feature,
            'property_count':property_count,
      }
      return render(request,"adminaccount/index.html",context)

@login_required()
def upload(request):
      form = UploadProperty()
      if request.method == "POST":
            form = UploadProperty(request.POST, request.FILES)
            if form.is_valid():
                  form.save()
                  return redirect('property-list')
      context = {
            'form':form
      }
      return render(request,"adminaccount/upload_property.html",context)

@login_required()
def propertyListAd(request):
      list = UploadProperties.objects.all()
      context = {
            'list':list
      }

      return render(request,"adminaccount/property_list.html",context)

@login_required()
def propertyEdit(request, pk):
      property = UploadProperties.objects.get(id=pk)
      form = UploadProperty(instance=property)
      if request.method == "POST":
            form = UploadProperty(request.POST,request.FILES,instance=property)
            if form.is_valid():
                  form.save()
                  return redirect('property-list')
      context = {
            'form':form
      }
      return render(request,"adminaccount/upload_property.html",context)


@login_required()
def deleteProrperty(request,pk):
      property = UploadProperties.objects.get(id=pk)
      if request.method == "POST":
            property.delete()
            return redirect('property-list')
      context = {
            'property':property
      }
      return render(request,"adminaccount/delete.html",context)