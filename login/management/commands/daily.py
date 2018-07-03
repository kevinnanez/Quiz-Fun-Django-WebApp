from login.models import UserProfile


def dailycoins():
    queryset = UserProfile.objects.filter(coins__lte=9).update(daily=True)
    queryset = UserProfile.objects.filter(coins__lte=9).update(coins=10)
