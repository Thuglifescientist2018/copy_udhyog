from django.shortcuts import render
from .forms import SalesModelForm
from .models import Sales
# Create your views here.


def sales_home(request):
    template_name = "sales_home.html"
    salesForm1 = SalesModelForm(request.POST or None)
    if salesForm1.is_valid():
        salesForm1.save()
        salesForm1 = SalesModelForm()

    context = {
        "form1": salesForm1
    }
    return render(request, template_name, context)


def sales_list(request):
    template_name = "sales_list.html"
    sales = Sales.objects.all()
    context = {
        "sales": sales
    }
    return render(request, template_name, context)
