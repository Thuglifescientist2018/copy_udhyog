from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PurchasesModelForm
from .models import Purchases, TotalAmount
from django import forms
# Create your views here.


def purchases_home(request):
    print("list url: ", request.path)
    purchasesForm1 = PurchasesModelForm(request.POST or None)
    if purchasesForm1.is_valid():
        purchasesForm1.save()
        purchasesForm1 = PurchasesModelForm()

    context = {
        "form1": purchasesForm1,

    }
    template_name = "purchases.html"
    return render(request, template_name, context)


def purchases_list(request):
    purchases_list = Purchases.objects.all().order_by("-date")
    purchases_total = Purchases.total_price()
    count = purchases_list.count
    paginator = Paginator(purchases_list, 2)
    page = request.GET.get('page')
    try:
        purchases = paginator.page(page)
    except PageNotAnInteger:
        purchases = paginator.page(1)
    except EmptyPage:
        purchases = paginator.page(paginator.num_pages)

    context = {
        "purchases": purchases,
        "count": count,
        "total_price": purchases_total,



    }
    template_name = "purchases_list.html"
    return render(request, template_name, context)


def purchase_edit(request, slug):
    template_name = "purchase_edit.html"
    purchase = Purchases.objects.filter(slug=slug).first()
    purchases_edit_form = PurchasesModelForm(
        request.POST or None, instance=purchase)

    if purchases_edit_form.is_valid():
        purchases_edit_form.save()
        try:
            if purchase.slug:
                return redirect("/purchases/edit/{0}".format(purchase.slug))
        except AttributeError:
            return HttpResponse("Page not Found")

    context = {
        "form": purchases_edit_form
    }
    return render(request, template_name, context)


def purchase_delete(request, slug):
    template_name = "purchase_delete.html"
    purchase = Purchases.objects.filter(slug=slug).first()
    if request.method == "POST":
        purchase.delete()
        return redirect('/purchases/list')
    context = {
        "purchase": purchase
    }
    return render(request, template_name, context)
