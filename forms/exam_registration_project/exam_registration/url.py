from django.urls import path
from .import views
from .views import exam_registration, success_view

urlpatterns = [
    path("exam_registration", views.exam_registration, name='exam'),
    path("success/", views.success_view, name='success')
]