from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices
# Create your views here.
def index(request):
    listing = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listing,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices  

    }
    return render(request, 'pages/index.html', context)


def about(request):
    Realtors = Realtor.objects.order_by('-hire_date')
    MVP_realtor = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': Realtors,
        'mvp_realtor': MVP_realtor
    }
    return render(request, 'pages/about.html', context)