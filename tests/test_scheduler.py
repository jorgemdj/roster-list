import unittest
from src.models import Employee, Shift, WeekDay
from src.scheduler import RosterScheduler

class TestRosterScheduler(unittest.TestCase):
    def setUp(self):
        # Create a test set of employees
        self.employees = [
            Employee(
                name="John",
                morning_only=True,
                unavailable_days=[WeekDay.SUNDAY]
            ),
            Employee(
                name="Maria",
                preferred_shifts=[Shift.AFTERNOON]
            ),
            Employee(
                name="Bob",
                preferred_shifts=[Shift.MORNING, Shift.AFTERNOON]
            )
        ]
        self.scheduler = RosterScheduler(self.employees)

    def test_schedule_creation(self):
        schedule = self.scheduler.generate_weekly_schedule()
        # Test if schedule contains all days
        self.assertEqual(len(schedule), len(WeekDay))
        
        # Test if each day has all shifts
        for day in WeekDay:
            self.assertIn(Shift.MORNING, schedule[day])
            self.assertIn(Shift.AFTERNOON, schedule[day])
            self.assertIn(Shift.DAY_OFF, schedule[day])

    def test_morning_only_restriction(self):
        schedule = self.scheduler.generate_weekly_schedule()
        for day in WeekDay:
            if day != WeekDay.SUNDAY:  # John is unavailable on Sunday
                afternoon_workers = schedule[day][Shift.AFTERNOON]
                self.assertNotIn("John", [emp.name for emp in afternoon_workers])

    def test_weekend_afternoon_restriction(self):
        schedule = self.scheduler.generate_weekly_schedule()
        saturday_afternoon = schedule[WeekDay.SATURDAY][Shift.AFTERNOON]
        sunday_afternoon = schedule[WeekDay.SUNDAY][Shift.AFTERNOON]
        
        # Check that no employee works both Saturday and Sunday afternoon
        saturday_names = {emp.name for emp in saturday_afternoon}
        sunday_names = {emp.name for emp in sunday_afternoon}
        self.assertEqual(saturday_names.intersection(sunday_names), set())

if __name__ == '__main__':
    unittest.main()