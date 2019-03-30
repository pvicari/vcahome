from django.shortcuts import render
from django.utils import timezone
from .models import Card

# Create your views here.

def card_list(request):
    cards = Card.objects.all().order_by('created_date')
    return render(request, 'linkeep/card_list.html', {'cards': cards})
