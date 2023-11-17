from django.urls import path
from my_app.views import (service_view,detail_view,login_view,logout_view,
                          blog_view,blog_detail_view,about_view,index_view,
                          contact_view,quote_view,testimonial_view,team_view,)


urlpatterns = [

path('service/',service_view,name = 'service'),
path('detail/<slug>/',detail_view,name = 'detail'),
path('login/',login_view,name = 'login'),
path('logout/',login_view,name = 'logout'),
path('blog/',blog_view,name = 'blog'),
path('about/',about_view,name = 'about'),
path('blog/detail/<slug>',blog_detail_view,name = 'blog_detail'),
path('',index_view,name = 'index'),
path('contact/',contact_view,name = 'contact'),
path('quote/',quote_view,name = 'quote'),
path('testimonial/',testimonial_view,name = 'testimonial'),
path('team/',team_view,name = 'team'),


]
