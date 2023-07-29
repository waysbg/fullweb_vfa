from django.urls import path, include
from fullweb.bills import views

urlpatterns = [
    path('', views.ListBillsView.as_view(), name='bills list'),
    path('create/', views.CreateBillView.as_view(), name='bill create'),
    path('edit/<int:bill_pk>/', views.edit_bill, name='bill edit'),
    path('delete/<int:bill_pk>/', views.delete_bill, name='bill delete'),
]