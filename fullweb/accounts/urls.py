from django.urls import path, include
from fullweb.accounts import views

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='sign up'),
    path('sign-in/', views.SignInView.as_view(), name='sign in'),
    path('sign-out/', views.SignOutView.as_view(), name='sign out'),
    path('profile/<int:pk>/', include([
        path('', views.ProfileDetailsView.as_view(), name='profile details'),
        path('edit/', views.ProfileEditView.as_view(), name='profile edit'),
        path('delete/', views.ProfileDeleteView.as_view(), name='profile delete'),
        path('password/', views.ProfilePasswordView.as_view(), name='password change'),
    ])),
]