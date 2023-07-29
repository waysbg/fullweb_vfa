from django.urls import path, include
from fullweb.common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.important, name='important'),
    path('staff/', views.staff_section, name='admin site'),
    path('delete/', views.users_delete, name='users delete'),
]