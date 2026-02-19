from datetime import date, timedelta
from scaledown.models import DailyHealthRecord
import random

def generate_sample_data(days=365):
    records = []
    start = date.today() - timedelta(days=days)

    for i in range(days):
        records.append(
            DailyHealthRecord(
                day=start + timedelta(days=i),
                steps=random.randint(3000, 12000),
                avg_hr=random.uniform(60, 95),
                sleep_hours=random.uniform(4.5, 8.5),
                calories=random.randint(1800, 2800)
            )
        )
    return records
