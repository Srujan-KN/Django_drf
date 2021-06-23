from django.contrib import admin
from django.urls import path
from rest.views import TestView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add',TestView.as_view(),name='test')
]
