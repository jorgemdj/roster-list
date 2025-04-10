from models import Employee, Shift, WeekDay
from scheduler import RosterScheduler

def main():
    # Example of how to use the system
    employees = [
        Employee(
            name="John",
            morning_only=True,
            unavailable_days=[WeekDay.SUNDAY]
        ),
        Employee(
            name="Maria",
            preferred_shifts=[Shift.AFTERNOON]
        ),
        # Add more employees
    ]

    scheduler = RosterScheduler(employees)
    weekly_schedule = scheduler.generate_weekly_schedule()

    # Print or export the schedule
    for day in WeekDay:
        print(f"\n{day.name}:")
        for shift in Shift:
            print(f"{shift.name}: {weekly_schedule[day][shift]}")

if __name__ == "__main__":
    main()