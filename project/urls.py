"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views, urls

# Path es cada link
# Include() importa URLS internas propias de la app. 
# Hay que crear urls.py en la app, y crear otra lista urlpatterns con las URL internas.
urlpatterns = [
    path('admin/', admin.site.urls),        #localhost/admin
    path('blog/', views.index),
    path('HolaMundo/', views.HolaMundo),    #localhost/HolaMundo/
    path('otros/', include('blog.urls'))    #localhost/otros/auxiliar1  ;   #localhost/otros/auxiliar2
]
