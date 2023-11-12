from django.shortcuts import render
from Offers.models import Offer

def add_offer_page(request):
    return render(request, 'Offers/add_offer.html')

def add_offer(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_description = request.POST.get('item_description')
        item_image = request.FILES['item_image']
        item_price = request.POST.get('item_price')

        offer = Offer(
            item_name=item_name,
            item_description=item_description,
            item_image=item_image,
            item_price=item_price
        )
        offer.save()
        return render(request, 'Core/index.html')
    return render(request, 'Core/index.html')
