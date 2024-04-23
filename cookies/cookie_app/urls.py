from django import path
from .import views

urlpatterns=[
    path('set-cookies/',views.set-cookies, name='set-cookies'),
    path('get-cookies/', views.get-cookies, name='get-cookies'),
    path('delete-cookie/', views.delete-cookies, name='delete-cookies'),
    path('set-session/', views.set-session, name='set-session'),
    # path('set-cookie/', views.set - cookies, name='set-cookies'),
    # path('set-cookie/', views.set - cookies, name='set-cookies')

]