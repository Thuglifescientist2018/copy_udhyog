from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
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
    sales_list = Sales.objects.all().order_by('-date')
    count = sales_list.count
    paginator = Paginator(sales_list, 2)
    page = request.GET.get('page')
    try:
        sales = paginator.page(page)
    except PageNotAnInteger:
        sales = paginator.page(1)
    except EmptyPage:
        sales = paginator.page(paginator.num_pages)

    def total_price():
        price = 0
        for sale in sales_list:
            price += float(sale.actual_price())

        return price

    context = {
        "sales": sales,
        "count": count,
        "total_price": total_price(),

    }
    return render(request, template_name, context)


def sale_edit(request, slug):
    template_name = "sale_edit.html"
    sale = Sales.objects.filter(slug=slug).first()
    sale_edit_form = SalesModelForm(
        request.POST or None, instance=sale)

    if sale_edit_form.is_valid():
        sale_edit_form.save()
        try:
            if sale.slug:
                return redirect("/sales/edit/{0}".format(sale.slug))
        except AttributeError:
            return HttpResponse("Page not Found")

    context = {
        "form": sale_edit_form
    }
    return render(request, template_name, context)


def sale_delete(request, slug):
    template_name = "sale_delete.html"
    sale = Sales.objects.filter(slug=slug).first()
    if request.method == "POST":
        sale.delete()
        return redirect('/sales/list')
    context = {
        "sale": sale
    }
    return render(request, template_name, context)
