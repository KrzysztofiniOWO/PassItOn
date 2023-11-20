from django.shortcuts import render
from Offers.models import Offer

def index(request):
    offers = Offer.objects.all().order_by('-item_name')[:10]
    return render(request, 'Core/index.html', {'offers': offers})