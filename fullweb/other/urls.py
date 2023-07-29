from django.urls import path, include
from fullweb.other import views

urlpatterns = [
    path('', views.ListOtherView.as_view(), name='other list'),
    path('create/', views.CreateOtherView.as_view(), name='other create'),
    path('edit/<int:other_pk>/', views.edit_other, name='other edit'),
    path('delete/<int:other_pk>/', views.delete_other, name='other delete'),
]