from django.urls import path
from .views import sale_delete, sale_edit, sales_home, sales_list

urlpatterns = [
    path('', sales_home),
    path('list/', sales_list),
    path('edit/<str:slug>/', sale_edit),
    path('delete/<str:slug>/', sale_delete)

]
