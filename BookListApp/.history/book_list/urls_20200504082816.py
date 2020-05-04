from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
	path('delete/<book_id>', views.delete, name='delete'),
	path('cross_off/<book_id>', views.cross_off, name='cross_off'),
	path('uncross/<book_id>', views.uncross, name='uncross'),
	path('edit/<book_id>', views.edit, name='edit'),    

]
