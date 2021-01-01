from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('order-summary/<order_id>', views.display_order),
    path('checkout/', views.process_order),
]
