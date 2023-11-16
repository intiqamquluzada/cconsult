from django.contrib import admin
from my_app.models import *

admin.site.register(Team)
admin.site.register(Testimonial)
admin.site.register(Comment)
admin.site.register(AboutModel)
admin.site.register(AboutSideBar)
admin.site.register(HomeSlider)
admin.site.register(Subscribe)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','image', 'slug', 'updated_at', 'created_at')

admin.site.register(Service,ServiceAdmin)

class QuotaAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','service', 'slug', 'updated_at', 'created_at')

admin.site.register(Quota,QuotaAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','subject', 'mesage', 'slug', 'updated_at', 'created_at')

admin.site.register(Contact,ContactAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','image', 'slug', 'updated_at', 'created_at')

admin.site.register(Blog,BlogAdmin)



