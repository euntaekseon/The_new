from django.urls import path
from django.views.generic import TemplateView
from . import views
 
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('signup_success/', TemplateView.as_view(template_name='account/signup_success.html'), name='signup_success'),
]
