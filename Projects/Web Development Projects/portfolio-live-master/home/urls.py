from django.contrib import admin
from django.urls import path, include
from home import views

# Django admin header Customization

admin.site.site_header = "Saurav Website"
admin.site.set_title = "Welcome to Saurav's Dashboard"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path('', views.main, name='main'),


]
