from django.contrib import admin
from django.urls import path
import wordcountapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcountapp.views.save, name='save'),
    path('result/', wordcountapp.views.result, name="result"),
]
