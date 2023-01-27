from uuid import UUID

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from datacenter.models import Passcard, Visit


def passcard_info_view(request: HttpRequest, passcode: UUID) -> HttpResponse:
    this_passcard_visits = []
    passcard = get_object_or_404(Passcard, passcode=passcode)
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
