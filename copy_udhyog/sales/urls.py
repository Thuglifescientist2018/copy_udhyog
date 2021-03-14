from django.urls import path
from .views import sales_home, sales_list

urlpatterns = [
    path('', sales_home),
    path('list/', sales_list)
]
