from animais.views import index
from django.contrib import admin
from django.urls import path
from animais.views import index
urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls)
]
