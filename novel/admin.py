from django.contrib import admin

# Register your models here.
# Developed by Surfa
from django.contrib import admin
from novel.models import Gallery, Contact, Bod
from novel.forms import ContactForm
# Register your models here.

class BodAdmin(admin.ModelAdmin):
    list_display = ('title','name','about','image',)
    search_fields = ['title', 'name','image']

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','image', 'image2',)
    search_fields = ['title','image',]

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','message')
    contact = ContactForm
    search_fields = ['name', 'email','message']

admin.site.register(Gallery, PostAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Bod, BodAdmin)

