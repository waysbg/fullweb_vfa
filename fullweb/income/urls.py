from django.urls import path, include
from fullweb.income import views

urlpatterns = [
    path('', views.ListIncomeView.as_view(), name='income list'),
    path('create/', views.CreateIncomeView.as_view(), name='income create'),
    path('edit/<int:income_pk>/', views.edit_income, name='income edit'),
    path('delete/<int:income_pk>/', views.delete_income, name='income delete'),
]