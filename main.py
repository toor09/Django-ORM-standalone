import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    pass_cards = Passcard.objects.all()
    first_pass_card = pass_cards[0]
    print(
        f"""
        owner_name: {first_pass_card.owner_name}
        passcode: {first_pass_card.passcode}
        created_at: {first_pass_card.created_at}
        is_active: {first_pass_card.is_active}
        """
    )
    active_pass_cards = Passcard.objects.filter(is_active=True)
    print(f"Все пропуски: {pass_cards}")  # noqa: T001
    print(f"Всего пропусков: {Passcard.objects.count()}")  # noqa: T001
    print(f"Активных пропусков: {len(active_pass_cards)}")  # noqa: T001
