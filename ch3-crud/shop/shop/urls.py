"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from crud.views import PostView,GetView, DeleteView ,PutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',PostView.as_view(),name='post'),
    path('product/<int:pk>/',GetView.as_view(),name='get'),
    path('product/delete/<int:pk>/',DeleteView.as_view(),name='delete'),
    path('product/update/<int:pk>/',PutView.as_view(),name='put')
]
