from dataclasses import dataclass
from datetime import date

@dataclass
class DailyHealthRecord:
    day: date
    steps: int
    avg_hr: float
    sleep_hours: float
    calories: int

@dataclass
class HealthState:
    period: str
    avg_steps: int
    avg_hr: float
    avg_sleep: float
    trend: str
    flags: list
