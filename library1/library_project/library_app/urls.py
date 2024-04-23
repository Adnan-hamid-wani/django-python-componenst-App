from django.urls import views
from .import views

urlpatterns = [
    path("", views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('books', views.books, name='books')

]