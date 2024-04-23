from django.urls import path
from .import views
urlpatterns = [
    path('successful/', views.successful),
    path('created/', views.created),
    path('accepted/', views.accepted),
    path('non-authorization-info/', views.non_authorization_info),
    path('found/', views.found),
    path('bad-request/', views.bad_request),
    path('unauthorized/', views.unauthorized),
    path('payment-required/', views.payment_required),
    path('not-found/', views.not_found),

]