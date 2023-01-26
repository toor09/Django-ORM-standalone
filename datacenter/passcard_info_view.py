from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = Passcard.objects.get(passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard__passcode=passcode)
    for passcard_visit in passcard_visits:
        this_passcard_visits.append(
            {
                'entered_at': passcard_visit.get_local_entered_at(),
                'duration': passcard_visit.format_duration(passcard_visit.get_duration()),
                'is_strange': passcard_visit.is_visit_long(),
            }
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
