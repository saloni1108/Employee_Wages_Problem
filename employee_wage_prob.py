import random

class Employee:
    def __init__(self) -> None:
        self.WAGE_PER_HOUR = 20
        self.HOUR_PER_DAY = 8
        self.PART_TIME_HOUR = 4
        self.MAX_HOURS = 100
        self.MAX_DAYS = 20
        self.DAYS = 20

    def daily_wages(self, wage, hour):
        self.total_wages = wage * hour
        print("Daily Wage is: ", self.total_wages)

    def parttime_wage(self, wage, total):
        self.total_wages = wage * total
        print("Daily Wage is: ", self.total_wages)

    def monthly_wage(self, wage, hours, days):
        self.monthly_wages = wage * hours * days
        print("Monthly Wage is: ", self.monthly_wages)

    def check_attendance(cls):
        TOTAL_HOURS_WORKED = 0
        TOTAL_DAYS_WORKED = 0
        while TOTAL_HOURS_WORKED < cls.MAX_HOURS and TOTAL_DAYS_WORKED < cls.MAX_DAYS:
            attendance_chk = random.randint(0,2)
            match attendance_chk:
                case 1:
                    print("Employee is present for full time")
                    TOTAL_DAYS_WORKED += 1
                    TOTAL_HOURS_WORKED += cls.HOUR_PER_DAY
                    cls.daily_wages(cls.WAGE_PER_HOUR, cls.HOUR_PER_DAY)
                case 2:
                    print("Employee is present but for part-time")
                    TOTAL_DAYS_WORKED += 1
                    TOTAL_HOURS_WORKED += cls.PART_TIME_HOUR
                    cls.daily_wages(cls.WAGE_PER_HOUR, cls.PART_TIME_HOUR)
                case _:
                    print("Employee is absent")
                    TOTAL_DAYS_WORKED += 1
                    TOTAL_HOURS_WORKED += 0
        cls.monthly_wage(cls.WAGE_PER_HOUR, TOTAL_HOURS_WORKED, TOTAL_DAYS_WORKED)
        cls.total_working_hours(TOTAL_HOURS_WORKED)
    def total_working_hours(self, hours):
        print("total hour: ", hours)
John = Employee()
print("\tJohn's Wage: \n")
print(John.check_attendance())

Aviyana = Employee()
print("\n\n\t Aviyana's Wage: \n")
print(Aviyana.check_attendance())

Arianna = Employee()
print("\n\n\t Arianna's Wage: \n")
print(Arianna.check_attendance())
 
