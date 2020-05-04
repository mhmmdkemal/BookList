from django.contrib import admin
from django.urls import path, include
from book_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book_list.urls')),
]
