"""shorturl_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from shorturl_app import views

urlpatterns = [
    # path('create/', views.create_short_url, name='create_short_url'),
    # path('create/', views.create_snippet, name='create_snippet'),
    # path('display-data/', views.display_data, name='display_data'),
    path('', views.index, name='index'),
    path('<str:short_code>', views.redirect_to_full_url, name='redirect_to_full_url'),
    path('create/', views.create_snippet, name='create_snippet'),    
    path('view/<int:snippet_id>/', views.view_snippet, name='view_snippet'),
# scraper/urls.py

    path("display/", views.display_data, name="display_data"),
]