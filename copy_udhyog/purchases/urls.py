from django.urls import path
from .views import purchase_edit, purchases_home, purchases_list, purchase_delete

urlpatterns = [

    path('', purchases_home),
    path('list/', purchases_list),
    path('edit/<str:slug>/', purchase_edit),
    path('delete/<str:slug>/', purchase_delete)

]
