from django.urls import path
from my_app.views import service_view,detail_view,login_view,logout_view,blog_view,blog_detail_view


urlpatterns = [

path('service/',service_view,name = 'service'),
path('detail/<slug>/',detail_view,name = 'detail'),
path('login/',login_view,name = 'login'),
path('logout/',login_view,name = 'logout'),
path('blog/',blog_view,name = 'blog'),
path('blog/detail/<slug>',blog_detail_view,name = 'blog_detail'),


]
