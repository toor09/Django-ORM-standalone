from datetime import datetime, timedelta

from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self) -> timedelta:
        if self.leaved_at:
            return localtime(self.leaved_at) - localtime(self.entered_at)
        return localtime() - localtime(self.entered_at)

    def get_local_entered_at(self) -> datetime:
        return localtime(self.entered_at)

    def is_visit_long(self, minutes: int = 60) -> bool:
        if self.leaved_at:
            delta = localtime(self.leaved_at) - localtime(self.entered_at)
            return delta.total_seconds() > minutes * 60
        return False

    @staticmethod
    def format_duration(duration: timedelta) -> str:
        seconds = duration.total_seconds()
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f'{hours:.0f}ч:{minutes:.0f}мин'

    def __str__(self) -> str:
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    class Meta:
        ordering = ['-entered_at']
