from django.urls import path, include
from fullweb.daily import views

urlpatterns = [
    path('', views.ListDailyView.as_view(), name='daily list'),
    path('create/', views.CreateDailyView.as_view(), name='daily create'),
    path('edit/<int:daily_pk>/', views.edit_daily, name='daily edit'),
    path('delete/<int:daily_pk>/', views.delete_daily, name='daily delete'),
]