from django.shortcuts import render

# Create your views here.

def card_list(request):
    return render(request, 'linkeep/card_list.html', {})
    