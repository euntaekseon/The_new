from django.urls import path
from django.views.generic import TemplateView
from . import views
 
urlpatterns = [
    path('board/', views.board, name='board'),
    path('about/', views.about, name='about'),
    path('detail/<int:post_id>', views.detail, name = 'detail'),
    path('creating/', views.creating, name='creating'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('<int:post_id>/like/', views.like, name='like'),
    path('mypage/<int:user_id>', views.mypage, name='mypage'),
]
