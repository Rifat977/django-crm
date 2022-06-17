from django.urls import path
from . import views

app_name="accounts"
urlpatterns = [
    path('', views.home, name="dashboard"),
    path('product/', views.product, name="product"),
    path('customer/', views.customer, name="customer")
]
