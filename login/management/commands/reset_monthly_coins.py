from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from login.management.commands.monthly import reset_monthly_coins


class Command(BaseCommand):
    help = 'reset monthly coins'

    def handle(self, *args, **kwargs):
        reset_monthly_coins()
