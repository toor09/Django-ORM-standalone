from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from datacenter.models import Passcard


def active_passcards_view(request: HttpRequest) -> HttpResponse:
    active_pass_cards = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': active_pass_cards,
    }
    return render(request, 'active_passcards.html', context)
