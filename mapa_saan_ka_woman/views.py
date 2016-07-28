from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import OrderInfo


# Create your views here.
def site_location(request):
    orders = OrderInfo.objects.all()
    
    for orde in orders:
        print(orde.drop_off_address)
    context = {
        'orders': orders,
    }
    return render(request, 'mapa_saan_ka_woman/site_location.html', context)