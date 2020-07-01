from django.db import models
from django.db.models.signals import pre_save
from estate.utils import unique_slug_generator
from django.contrib.auth import get_user_model

User = get_user_model()



LISTING_TYPE = (
      ('rent','rent'),
      ('sale','sale')
)

PROPERTY_TYPE = (
      ('apartment','apartment'),
      ('commercial','commercial'),
      ('office','office'),
      ('land','land'),
)

ROOFING = (
      ('new','new'),
      ('old','old')
)

BED_ROOMS = (
      ('1','1'),
      ('2','2'),
      ('3','3'),
      ('4','4'),
      ('5','5'),
      ('6','6'),
      ('7','7'),
      ('8','8'),
      ('9','9'),
      ('10','10'),
)
BED = (
      ('1','1'),
      ('2','2'),
      ('3','3'),
      ('4','4'),
      ('5','5'),
      ('6','6'),
      ('7','7'),
      ('8','8'),
      ('9','9'),
      ('10','10'),
)

BATH_ROOMS = (
      ('1','1'),
      ('2','2'),
      ('3','3'),
      ('4','4'),
      ('5','5'),
      ('6','6'),
      ('7','7'),
      ('8','8'),
      ('9','9'),
      ('10','10'),
)

TOILET = (
      ('1','1'),
      ('2','2'),
      ('3','3'),
      ('4','4'),
      ('5','5'),
      ('6','6'),
      ('7','7'),
      ('8','8'),
      ('9','9'),
      ('10','10'),
)

GARAGE = (
      ('1','1'),
      ('2','2'),
      ('3','3'),
      ('4','4'),
      ('5','5'),
      ('6','6'),
      ('7','7'),
      ('8','8'),
      ('9','9'),
      ('10','10'),
)

COMMISSION = (
      ('10','10'),
      ('20','20'),
      ('30','30'),
      ('40','40'),
      ('50','50'),
      ('60','60'),
      ('70','70'),
      ('80','80'),
)

STATES = (
      ('Abuja','Abuja'),
      ('Abia','Abia'),
      ('Adamawa','Adamawa'),
      ('Akwa Ibom','Akwa Ibom'),
      ('Anambra','Anambra'),
      ('Bauchi','Bauchi'),
      ('Bayelsa','Bayelsa'),
      ('Benue','Benue'),
      ('Borno','Borno'),
      ('Cross River','Cross River'),
      ('Delta','Delta'),
      ('Ebonyi','Ebonyi'),
      ('Edo','Edo'),
      ('Ekiti','Ekiti'),
      ('Enugu','Enugu'),
      ('Gombe','Gombe'),
      ('Imo','Imo'),
      ('Jigawa','Jigawa'),
      ('Kaduna','Kaduna'),
      ('Kano','Kano'),
      ('Katsina','Katsina'),
      ('Kebbi','Kebbi'),
      ('Kogi','Kogi'),
      ('Kwara','Kwara'),
      ('Lagos','Lagos'),
      ('Nassarawa','Nassarawa'),
      ('Niger','Niger'),
      ('Ogun','Ogun'),
      ('Ondo','Ondo'),
      ('Osun','Osun'),
      ('Oyo','Oyo'),
      ('Plateau','Plateau'),
      ('Rivers','Rivers'),
      ('Sokoto','Sokoto'),
      ('Taraba','Taraba'),
      ('Yobe','Yobe'),
      ('Zamfara','Zamfara')
)

SECURITY = (
      ('yes','yes'),
      ('no','no')
)

TAG = (
      ('featured','featured'),
      ('popular','popular')
)

PAYMENT = (
      ('yearly','yearly'),
      ('monthly','monthly')
)


class Manager(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
      profile_img = models.ImageField()

      def __str__(self):
            return self.user

class Amentities(models.Model):
      amentity = models.CharField(max_length=300,null=True)

      def __str__(self):
            return self.amentity

class Tag(models.Model):
      tag = models.CharField(choices=LISTING_TYPE ,max_length=300,null=True)

      def __str__(self):
            return self.tag

class UploadProperties(models.Model):
      property_title = models.CharField(max_length=300,null=True)
      slug = models.SlugField(max_length=300,null=True,blank=True)
      property_price = models.IntegerField(null=True)
      payment_condition = models.CharField(choices=PAYMENT,max_length=30,null=True)
      commission = models.CharField(choices=COMMISSION,max_length=30,null=True)
      listing_type = models.CharField(choices=LISTING_TYPE,max_length=10,null=True)
      tag = models.CharField(choices=TAG,max_length=10,null=True)
      property_type = models.CharField(choices=PROPERTY_TYPE,max_length=30,null=True)
      date_built = models.DateField(auto_now_add=True,null=True)
      bedrooms = models.CharField(choices=BED_ROOMS,max_length=10,null=True)
      bathrooms = models.CharField(choices=BATH_ROOMS,max_length=10,null=True)
      toilet = models.CharField(choices=TOILET,max_length=10,null=True)
      garage = models.CharField(choices=GARAGE,null=True,max_length=10)
      amentities = models.ManyToManyField(Amentities)
      address = models.CharField(max_length=400,null=True)
      plot_of_land = models.CharField(max_length=400,null=True)
      office_space = models.CharField(max_length=400,null=True)
      state = models.CharField(choices=STATES,max_length=40,null=True)
      security = models.CharField(choices=SECURITY,max_length=10,null=True)
      description = models.TextField(null=True)
      time_uploaded = models.DateTimeField(auto_now_add=True, null=True)
      property_main_image = models.ImageField(upload_to='properties_images/',null=True,blank=True)
      property_image2 = models.ImageField(upload_to='properties_images/',null=True,blank=True)
      property_image3 = models.ImageField(upload_to='properties_images/',null=True,blank=True)
      property_image4 = models.ImageField(upload_to='properties_images/',null=True,blank=True)
      property_image5 = models.ImageField(upload_to='properties_images/',null=True,blank=True)


      def __str__(self):
            return self.property_title
      

def slug_generator(sender, instance, *args, **kwargs):
      if not instance.slug:
            instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator, sender=UploadProperties)


class Newsletters(models.Model):
      email = models.EmailField()

      def __str__(self):
            return self.email


class Companyinformation(models.Model):
      company_name = models.CharField(max_length=200,null=True)
      company_address = models.CharField(max_length=300,null=True)
      company_state = models.CharField(choices=STATES,max_length=15,null=True)
      company_logo_light = models.ImageField(default="assets/anotherlogo.png",upload_to= 'company_logo/',null=True)
      company_logo_dark = models.ImageField(default="assets/anotherlogo1.png",upload_to= 'company_logo/' , null=True)
      company_phone_number1 = models.CharField(max_length=300,null=True)
      company_phone_number2 = models.CharField(max_length=300,null=True)
      company_address = models.CharField(max_length=300,null=True)
      company_email = models.EmailField(null=True)
      company_facebook_link = models.CharField(max_length=300,null=True)
      company_twitter_link = models.CharField(max_length=300,null=True)
      company_whatsapp_link = models.CharField(max_length=300,null=True)
      company_instagram_link = models.CharField(max_length=300,null=True)

      def __str__(self):
            return self.company_name

class HomePageImages(models.Model):
      slide_image1 = models.ImageField(default="media-demo/banner/banner-1.jpg",upload_to= 'homepage_images/',null=True)
      slide_image2 = models.ImageField(default="media-demo/banner/banner-1.jpg",upload_to= 'homepage_images/',null=True)
      slide_image3 = models.ImageField(default="media-demo/banner/banner-1.jpg",upload_to= 'homepage_images/',null=True)
      slide_image4 = models.ImageField(default="media-demo/banner/banner-1.jpg",upload_to= 'homepage_images/',null=True)
      company_image = models.ImageField(default="media-demo/banner/banner-1.jpg",upload_to= 'homepage_images/',null=True)


class Testmonials(models.Model):
      client_name = models.CharField(max_length=200,null=True)
      client_career = models.CharField(max_length=200,null=True)
      client_image = models.ImageField(default="img.png",upload_to= 'clients_images/',null=True)
      client_comment = models.TextField(null=True)

      def __str__(self):
            return self.client_name

class Workers(models.Model):
      staff_name = models.CharField(max_length=200,null=True)
      staff_image = models.ImageField(default="img.png",upload_to='staff_image/',null=True)
      staff_phoneNumber = models.CharField(max_length=15,null=True)
      staff_position = models.CharField(max_length=100,null=True)

      def __str__(self):
            return self.staff_name

class Partners(models.Model):
      partner_name = models.CharField(max_length=200,null=True)
      partner_logo = models.ImageField(upload_to= 'partners_logo/',null=True)

      def __str__(self):
            return self.partner_name






