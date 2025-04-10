from dataclasses import dataclass
from typing import List, Optional
from enum import Enum

class Shift(Enum):
    MORNING = "morning"
    AFTERNOON = "afternoon"
    DAY_OFF = "day_off"

class WeekDay(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

@dataclass
class Employee:
    name: str
    morning_only: bool = False
    preferred_shifts: List[Shift] = None
    unavailable_days: List[WeekDay] = None