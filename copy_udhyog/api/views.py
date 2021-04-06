
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PurchasesSerializer, SalesSerializer
from purchases.models import Purchases, TotalAmount

from sales.models import Sales


# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task_list',
        "some": "thing",
        "i": "can"
    }
    return Response(api_urls)


@api_view(['GET'])
def purchaseList(request):
    purchases = Purchases.objects.all()
    serializer = PurchasesSerializer(purchases, many=True)
    total_amount = TotalAmount.objects.all().last()
    total_amount = total_amount.total_amount
    purchases_item_count = purchases.count()
    return Response([{"total": str(total_amount), "count": purchases_item_count}, serializer.data])


@api_view(['GET'])
def salesList(request):
    sales = Sales.objects.all()
    serializer = SalesSerializer(sales, many=True)
    return Response(serializer.data)
