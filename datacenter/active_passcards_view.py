from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def active_passcards_view(request):
    active_pass_cards = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': active_pass_cards,
    }
    return render(request, 'active_passcards.html', context)
