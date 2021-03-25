from django.urls import path
from . import views

urlpatterns = [

    path('', views.apiOverview, name="api-overview"),
    path('purchase-list/', views.purchaseList, name="purchase-list"),
    path('sales-list/', views.salesList, name="sales-list")
]
