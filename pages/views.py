from django.shortcuts import render

from listings.models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices

from realtors.models import Realtor


# Create your views here.

from django.http import HttpResponse

def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,

    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Luam toti vanzatorii de case
    realtors = Realtor.objects.order_by('-hire_date')

    # Vanzatorul lunii

    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
    }

    return render(request, 'pages/about.html', context)
