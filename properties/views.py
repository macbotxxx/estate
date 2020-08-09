from django.shortcuts import render, get_object_or_404, redirect
from .models import UploadProperties, Tag, Newsletters, HomePageImages, Testmonials, Partners, Companyinformation, \
    Workers, Fqa, About
from .filters import PropertyFilter
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CompanyDetails, CompanyLogo, HomePageImage, QuestionAnswer, CompanyAbout, \
    UploadPropertyi, CompanyAbout, WorkersDetails, CustomerReviews
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

    return render(request, "main/request.htlm", {})


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

    return render(request, "main/contactus.html", {})


def home(request):
    aboutus = About.objects.all()
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
    myfilter = PropertyFilter(request.GET, queryset=search)
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
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=[to_email])
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
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=[to_email])
            html_template = get_template("emails/newsletter.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()

    context = {
        'aboutus': aboutus,
        'staff': staff,
        'partner': partner,
        'testimonies': testimonies,
        'slideImages': slideImages,
        'recentx': recentx,
        'list': list,
        'popular': popular,
        'featured': featured,
        'myfilter': myfilter,
        'recent': recent,
        'companydetails': companydetails,
    }
    return render(request, 'main/index.html', context)


def propertiesDetails(request, slug):
    aboutus = About.objects.all()
    recent = UploadProperties.objects.all().order_by('-time_uploaded')[:6]
    companydetails = Companyinformation.objects.all()
    details = get_object_or_404(UploadProperties, slug=slug)
    search = UploadProperties.objects.all()
    sale = UploadProperties.objects.filter(listing_type='sale').order_by('-time_uploaded')[:4]
    rent = UploadProperties.objects.filter(listing_type='rent').order_by('-time_uploaded')[:4]
    myfilter = PropertyFilter(request.GET, queryset=search)
    search = myfilter.qs
    tagx = Tag.objects.all()
    context = {
        'aboutus': aboutus,
        'recent': recent,
        'companydetails': companydetails,
        'tagx': tagx,
        'sale': sale,
        'rent': rent,
        'myfilter': myfilter,
        'details': details
    }
    return render(request, 'main/property_details.html', context)


def properties(request):
    aboutus = About.objects.all()
    recent = UploadProperties.objects.all().order_by('-time_uploaded')[:6]
    companydetails = Companyinformation.objects.all()
    allproperties = UploadProperties.objects.all().order_by('-time_uploaded')
    search = UploadProperties.objects.all()
    paginator = Paginator(allproperties, 9)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    myfilter = PropertyFilter(request.GET, queryset=search)
    search = myfilter.qs
    list = Tag.objects.all()
    # count = UploadProperties.objects.all().count()
    context = {
        'aboutus': aboutus,
        'recent': recent,
        'companydetails': companydetails,
        'page_obj': page_obj,
        'myfilter': myfilter,
        # 'count':count,
        'allproperties': allproperties,
        'list': list
    }
    return render(request, 'main/properties_listing.html', context)


def propertylist(request):
    aboutus = About.objects.all()
    recent = UploadProperties.objects.all().order_by('-time_uploaded')[:6]
    companydetails = Companyinformation.objects.all()
    list = Tag.objects.all()
    searchx = UploadProperties.objects.all()
    myfilter = PropertyFilter(request.GET, queryset=searchx)
    search = myfilter.qs
    paginator = Paginator(search, 9)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count = myfilter.qs.count()
    tagx = Tag.objects.all()
    context = {
        'page_obj':page_obj,
        'aboutus': aboutus,
        'recent': recent,
        'companydetails': companydetails,
        'tagx': tagx,
        'myfilter': myfilter,
        'search': search,
        'count': count,
        'list': list
    }
    return render(request, 'main/properties_search.html', context)


def listingType(request, tag):
    aboutus = About.objects.all()
    recent = UploadProperties.objects.all().order_by('-time_uploaded')[:6]
    companydetails = Companyinformation.objects.all()
    allproperties = UploadProperties.objects.filter(listing_type=tag)
    tagx = Tag.objects.all()
    search = UploadProperties.objects.all()
    myfilter = PropertyFilter(request.GET, queryset=search)
    search = myfilter.qs
    count = allproperties.count()
    email = Newsletters.objects.all()
    paginator = Paginator(allproperties, 9)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'recent': recent,
        'aboutus': aboutus,
        'companydetails': companydetails,
        'page_obj': page_obj,
        'email': email,
        'allproperties': allproperties,
        'tagx': tagx,
        'myfilter': myfilter,
        'count': count,
    }

    return render(request, 'main/property.html', context)


def contact(request):
    aboutus = About.objects.all()
    recent = UploadProperties.objects.all().order_by('-time_uploaded')[:6]
    companydetails = Companyinformation.objects.all()
    list = Tag.objects.all()
    context = {
        'aboutus': aboutus,
        'recent': recent,
        'companydetails': companydetails,
        'list': list,

    }
    return render(request, "main/contacts.html", context)


def aboutUs(request):
    aboutus = About.objects.all()
    staff = Workers.objects.all()[:3]
    recent = UploadProperties.objects.all().order_by('-time_uploaded')[:6]
    recentx = UploadProperties.objects.all().order_by('-time_uploaded')[:3]
    companydetails = Companyinformation.objects.all()
    list = Tag.objects.all()
    context = {
        'staff': staff,
        'aboutus': aboutus,
        'recent': recent,
        'recentx': recentx,
        'companydetails': companydetails,
        'list': list

    }
    return render(request, "main/about_us.html", context)


def testimonies(request):
    aboutus = About.objects.all()
    recent = UploadProperties.objects.all().order_by('-time_uploaded')[:6]
    companydetails = Companyinformation.objects.all()
    testimonies = Testmonials.objects.all()
    search = UploadProperties.objects.all()
    myfilter = PropertyFilter(request.GET, queryset=search)
    search = myfilter.qs
    list = Tag.objects.all()
    context = {
        'aboutus': aboutus,
        'recent': recent,
        'companydetails': companydetails,
        'testimonies': testimonies,
        'myfilter': myfilter,
        'list': list

    }
    return render(request, "main/reviews.html", context)


def featured(request):
    aboutus = About.objects.all()
    recent = UploadProperties.objects.all().order_by('-time_uploaded')[:6]
    companydetails = Companyinformation.objects.all()
    allproperties = UploadProperties.objects.filter(tag='featured')
    count = allproperties.count()
    paginator = Paginator(allproperties, 9)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    list = Tag.objects.all()
    search = UploadProperties.objects.all()
    myfilter = PropertyFilter(request.GET, queryset=search)
    search = myfilter.qs
    context = {
        'aboutus': aboutus,
        'recent': recent,
        'companydetails': companydetails,
        'page_obj': page_obj,
        'allproperties': allproperties,
        'myfilter': myfilter,
        'list': list,
        'count': count,
    }
    return render(request, "main/featured.html", context)


def faq(request):
    aboutus = About.objects.all()
    companydetails = Companyinformation.objects.all()
    recent = UploadProperties.objects.all().order_by('-time_uploaded')[:3]
    faqs = Fqa.objects.all()
    context = {
        'companydetails': companydetails,
        'aboutus': aboutus,
        'recent': recent,
        'faqs': faqs,

    }
    return render(request,"main/faq.html",context)

# ===============================================================================================================================================================
# ===========================================================ADMIN DASHBOARD FUNCTIONS ==========================================================================
# ***************************************************************************************************************************************************************

@login_required()
def adminhome(request):
    companyDetailz = Companyinformation.objects.all()
    property_count = UploadProperties.objects.count()
    property_feature = UploadProperties.objects.filter(tag='featured').count()
    subcribers = Newsletters.objects.count()
    xx = request.user
    context = {
        'subcribers': subcribers,
        'xx': xx,
        'property_feature': property_feature,
        'property_count': property_count,
        'companyDetailz': companyDetailz,

    }
    return render(request, "adminaccount/index.html", context)


@login_required()
def upload(request):
    companyDetailz = Companyinformation.objects.all()
    form = UploadPropertyi()
    if request.method == "POST":
        form = UploadPropertyi(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property-list')
        else:
            print('something is wrong with the coding')
    context = {
        'form': form,
        'companyDetailz': companyDetailz,

    }
    return render(request, "adminaccount/upload_property.html", context)


@login_required()
def propertyListAd(request):
    companyDetailz = Companyinformation.objects.all()
    list = UploadProperties.objects.all()
    context = {
        'list': list,
        'companyDetailz': companyDetailz,

    }

    return render(request, "adminaccount/property_list.html", context)


@login_required()
def propertyEdit(request, pk):
    companyDetailz = Companyinformation.objects.all()
    property = UploadProperties.objects.get(id=pk)
    form = UploadPropertyi(instance=property)
    if request.method == "POST":
        form = UploadPropertyi(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property-list')
    context = {
        'form': form,
        'companyDetailz': companyDetailz,

    }
    return render(request, "adminaccount/upload_property.html", context)


@login_required()
def deleteProrperty(request, pk):
    companyDetailz = Companyinformation.objects.all()
    property = UploadProperties.objects.get(id=pk)
    if request.method == "POST":
        property.delete()
        return redirect('property-list')
    context = {
        'property': property,
        'companyDetailz': companyDetailz,

    }
    return render(request, "adminaccount/delete.html", context)


@login_required()
def companydetails(request):
    companyDetailz = Companyinformation.objects.all()
    context = {
        'companyDetailz': companyDetailz,
        # 'form':form,
    }
    return render(request, "adminaccount/company_details.html", context)


@login_required()
def editcompanyDetails(request, pk):
    companyDetailz = Companyinformation.objects.all()
    companyDetail = Companyinformation.objects.get(id=pk)
    form = CompanyDetails(instance=companyDetail)
    if request.method == "POST":
        form = CompanyDetails(request.POST, instance=companyDetail)
        if form.is_valid():
            form.save()
            com_name = form.cleaned_data.get('company_name')
            messages.success(request, com_name + ' company details have been uploaded successfully  ')
            return redirect('company_details')
    context = {
        'form': form,
        'companyDetailz': companyDetailz,
    }
    return render(request, "adminaccount/edit_company_details.html", context)


@login_required()
def companylogoedit(request, pk):
    companyDetailz = Companyinformation.objects.all()
    companylogoz = Companyinformation.objects.get(id=pk)
    form = CompanyLogo(instance=companylogoz)
    if request.method == "POST":
        form = CompanyLogo(request.POST, request.FILES, instance=companylogoz)
        if form.is_valid():
            form.save()
            # com_name = form.cleaned_data.get('company_name')
            messages.success(request, '👍 Your company logo have been changed successfully  ')
            return redirect('/company_logo_edit/2/')
    context = {
        'form': form,
        'companyDetailz': companyDetailz,
    }
    return render(request, "adminaccount/edit_company_logo.html", context)


@login_required()
def companyimg(request, pk):
    companyDetailz = Companyinformation.objects.all()
    companylogo = HomePageImages.objects.all()
    companylogoz = HomePageImages.objects.get(id=pk)
    form = HomePageImage(instance=companylogoz)
    if request.method == "POST":
        form = HomePageImage(request.POST, request.FILES, instance=companylogoz)
        if form.is_valid():
            form.save()
            # com_name = form.cleaned_data.get('company_name')
            messages.success(request, '👍 Your company logo have been changed successfully  ')
            return redirect('/edit_image_slide/1/')
    context = {
        'companylogo': companylogo,
        'form': form,
        'companyDetailz': companyDetailz,
    }
    return render(request, "adminaccount/edit_home_slide.html", context)


@login_required()
def companyQues(request):
    getfaq = Fqa.objects.all()
    companyDetailz = Companyinformation.objects.all()
    form = QuestionAnswer()
    if request.method == "POST":
        form = QuestionAnswer(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '👍 Your have been uploaded  successfully  ')
    context = {
        'getfaq': getfaq,
        'form': form,
        'companyDetailz': companyDetailz,

    }
    return render(request, "adminaccount/questions.html", context)

@login_required()
def deletefaq(request, pk):
    if request.method == "POST":
        getfaq = Fqa.objects.get(id=pk)
        getfaq.delete()
        return redirect('/')
    context = {
        
    }
    return render(request, "adminaccount/off.html",context)

# handlinig the about us page 
@login_required()
def aboutuss(request):
    about = About.objects.all()
    companyDetailz = Companyinformation.objects.all()

    context = {
        'about': about,
        'companyDetailz':companyDetailz,
    }
    return render(request,'adminaccount/about.html',context)

@login_required()
def editAbout(request, pk):
    img = About.objects.all()
    about = About.objects.get(id= pk)
    form = CompanyAbout(instance=about)
    companyDetailz = Companyinformation.objects.all()
    if request.method == "POST":
        form = CompanyAbout(request.POST,request.FILES,instance=about)
        if form.is_valid():
            form.save()
            messages.success(request, '👍 it have been uploaded  successfully  ')
            return redirect('about-company')
    context = {
        'img': img,
        'about': about,
        'form': form,
        'companyDetailz':companyDetailz,

    }
    return render(request,'adminaccount/edit-about.html',context)


@login_required()
def worker(request):
    work = Workers.objects.all()
    companyDetailz = Companyinformation.objects.all()
    context = {
        'work': work,
        'companyDetailz':companyDetailz,
        
    }
    return render(request,"adminaccount/worker.html",context)

@login_required()
def editWorker(request, pk):
    companyDetailz = Companyinformation.objects.all()
    work = Workers.objects.get(id=pk)
    form = WorkersDetails(instance=work)
    if request.method == "POST":
        form = WorkersDetails(request.POST, request.FILES, instance=work)
        if form.is_valid():
            form.save()
            messages.success(request, '👍 it have been uploaded  successfully  ')
            return redirect('about-company')
    context = {
        'form': form,
        'companyDetailz':companyDetailz,

    }
    return render(request,"adminaccount/edit_worker.html", context)

# Testing the code using the testing view 

@login_required()
def text(request):
    return render(request,"adminaccount/text.html",{})

# Adding customers reviews 
@login_required()
def customerReviews(request):
    customersR = Testmonials.objects.all()
    context = {
        'customersR': customersR,
    }
    return render(request, "adminaccount/customerR.html",context)

@login_required()
def addingCusR(request):
    form = CustomerReviews()
    if request.method == "POST":
        form = CustomerReviews(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '👍 it have been uploaded  successfully  ')
            return redirect('cusR')
    context = {
        'form': form,
    }
    return render(request,"adminaccount/addcusR.html",context)

@login_required()
def editCusR(request, pk):
    CusR = Testmonials.objects.get(id= pk)
    form = CustomerReviews(instance=CusR)
    if request.method == "POST":
        form = CustomerReviews(request.POST, request.FILES, instance=CusR)
        if form.is_valid():
            form.save()
            messages.success(request, '👍 it have been uploaded  successfully  ')
            return redirect('cusR')
    context = {
        'form': form,
        'CusR':CusR,
    }
    return render(request,"adminaccount/addcusR.html",context)

@login_required()
def deleteCusR(request,pk):
    CusR = Testmonials.objects.get(id= pk)
    form = CustomerReviews(instance=CusR)
    if request.method == "POST":
        CusR.delete()
        messages.success(request, '👍 it have been uploaded  successfully  ')
        return redirect('cusR')
    context = {
        'CusR':CusR,
        'form':form,
    }    
    return render(request,"adminaccount/delCusR.html",context)

@login_required()
def subcribers(request):
    return render(request,"",{})




