from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from login.management.commands.daily import dailycoins


class Command(BaseCommand):
    help = 'gives daily coins'

    def handle(self, *args, **kwargs):
        dailycoins()
