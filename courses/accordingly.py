from django.core.management import BaseCommand
from django.db.models import Sum

from accounts.models import ProfileCustomUser

from covoiturage.courses.models import Reward


class Command(BaseCommand):
    help = 'Displays course details'

    def handle(self, *args, **options):
        drivers = ProfileCustomUser.objects.annotate(total_distance=Sum('trip__distance')).filter(
            total_distance__gt=1000000)
        for driver in drivers:
            if not Reward.objects.filter(driver=driver, reward_type='100000km ').exists():
                Reward.objects.create(driver=driver, reward_type='100000km ',
                                      description='Congratulation, you have 100000km distance ',)
                self.stdout.write(self.style.SUCCESS(f'Successfully added {driver}'))
            else:
                self.stdout.write(self.style.SUCCESS(self.style.NOTICE('You have 100000km distance reached already.')))