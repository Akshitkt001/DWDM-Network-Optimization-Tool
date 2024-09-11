from django.core.management.base import BaseCommand
from network_optimizer.algorithms.optimization import optimize_network

class Command(BaseCommand):
    help = 'Runs the DWDM network optimization algorithm'

    def handle(self, *args, **options):
        result = optimize_network()
        self.stdout.write(self.style.SUCCESS(result))