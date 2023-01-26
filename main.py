import os
import django
# from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
# execute_from_command_line('manage.py runserver 0.0.0.0:8000'.split())
django.setup()

from datacenter.models import Passcard  # noqa: E402
from datacenter.models import Visit  # noqa: E402

if __name__ == '__main__':
    pass_cards = Passcard.objects.all()
    first_pass_card = pass_cards[0]
    print(
        f'''
        owner_name: {first_pass_card.owner_name}
        passcode: {first_pass_card.passcode}
        created_at: {first_pass_card.created_at}
        is_active: {first_pass_card.is_active}
        '''
    )
    visits = Visit.objects.all()
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    print(active_visits)
    active_pass_cards = Passcard.objects.filter(is_active=True)

    print(f'Все визиты: {visits}')
    print(f'Все пропуски: {pass_cards}')  # noqa: T001
    print(f'Всего пропусков: {Passcard.objects.count()}')  # noqa: T001
    print(f'Активных пропусков: {len(active_pass_cards)}')  # noqa: T001
