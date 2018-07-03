from login.models import UserProfile


def reset_monthly_coins():
    queryset = UserProfile.objects.filter(coins__lte=9).update(daily=True)
    queryset = UserProfile.objects.filter(coins__lte=9).update(coins=0)
