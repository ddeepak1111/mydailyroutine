from django.core.management.base import BaseCommand
from datetime import date, timedelta
import random
from records.models import Record

class Command(BaseCommand):
    help = 'Generates dummy records'

    def handle(self, *args, **options):
        self.generate_dummy_records()

    def generate_dummy_records(self):
        for i in range(50):
            current_date = date.today() - timedelta(days=i)
            record = Record()
            record.recordid = current_date.strftime('%Y%m%d')
            record.sleep = random.choice(['1-3 Hrs', '3-5 Hrs', '5-7 Hrs', '7+ Hrs'])
            record.yoga = random.choice(['60', '45', '30', '15'])
            record.gym = random.choice(['60', '45', '30', '15'])
            record.walking = random.choice(['60', '45', '30', '15'])
            record.reading = random.choice(['60', '45', '30', '15'])
            record.skills_development = random.choice(['60', '45', '30', '15'])
            record.water_intake = random.choice(['3L', '2L', '1L'])
            record.expenses = random.randint(0, 100)
            record.todays_dairy = f"This is a dummy record for {current_date}"
            record.save()

            self.stdout.write(f"Created dummy record for {current_date}")
