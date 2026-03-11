# from django.urls import path
# from . import views
# urlpatterns = [
#     path('menu/',views.menu,name="menu"),
#     path('<int:chai_id>/',views.order_confirmation,name="order"),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),  # Menu page
    path('chai/<int:chai_id>/', views.order_confirmation, name='order_confirmation'),  # Order confirmation
     path('store/', views.store_location, name='store'),
]