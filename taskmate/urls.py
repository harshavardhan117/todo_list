
from django.contrib import admin
from django.urls import path,include
from todolist_app import views as todolist_app_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',todolist_app_views.index,name='index'),

    path('account/',include('users_app.urls') ),
    
    path('todolist/',include('todolist_app.urls') ),

    path('contact',todolist_app_views.contact,name='contact'),

    path('about-us',todolist_app_views.about,name='about'),
]
