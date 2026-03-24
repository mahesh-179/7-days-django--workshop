from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('edit/<int:tweet_id>/', views.tweet_edit, name='tweet_edit'),
    path('delete/<int:tweet_id>/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
    path('search/',views.search,name='search'),

    #AUTH
    path('login/', auth_views.LoginView.as_view(
        template_name='registeration/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]