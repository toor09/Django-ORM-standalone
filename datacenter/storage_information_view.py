from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from datacenter.models import Visit


def storage_information_view(request: HttpRequest) -> HttpResponse:
    non_closed_visits = []
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    for active_visit in active_visits:
        non_closed_visits.append(
            {
                'who_entered': active_visit.passcard.owner_name,
                'entered_at': active_visit.get_local_entered_at(),
                'duration': active_visit.format_duration(active_visit.get_duration()),
                'is_strange': active_visit.is_visit_long(active_visit.get_duration()),
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
