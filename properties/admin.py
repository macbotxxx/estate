from django.contrib import admin
from .models import UploadProperties, Amentities, Tag, Newsletters, Manager, HomePageImages, Testmonials, Workers, \
    Partners, Companyinformation
from ckeditor.widgets import CKEditorWidget
from .forms import UploadPropertyi


class PostAdmin(admin.ModelAdmin):
    form = UploadPropertyi


admin.site.register(UploadProperties, PostAdmin)
# admin.site.register(UploadProperties)
admin.site.register(Amentities)
admin.site.register(Tag)
admin.site.register(Newsletters)
admin.site.register(Manager)
admin.site.register(HomePageImages)
admin.site.register(Testmonials)
admin.site.register(Workers)
admin.site.register(Partners)
admin.site.register(Companyinformation)
