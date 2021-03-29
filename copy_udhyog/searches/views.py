

# Create your views here.
from django.shortcuts import render

# Create your views here.
from purchases.models import Purchases
from .models import SearchQuery


def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {"query": query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        purchases_list = Purchases.objects.search(query=query)
        context['purchases_list'] = purchases_list
        print(purchases_list)
    return render(request, 'searches/view.html', context)
