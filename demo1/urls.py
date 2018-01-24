from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('viewmenu', views.viewMenu, name='viewmenu'),
    path('viewMenuHTML', views.viewMenuHTML, name='viewMenuHTML'),
    path('addmenu', views.addmenu, name='addmenu'),
    path('login', auth_views.login, {'template_name': 'login.html'},name='login'),
    path('logout', auth_views.logout, {'next_page': '/demo1/'},name='logout'),
]
