from django.urls import path
from . import views
app_name = 'crud_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<str:title>', views.home_detail, name='blog_detail'),
    path('newblog', views.blog_create, name='newblog'),
    path('profile', views.profile, name='profile'),

]
