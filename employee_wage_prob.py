import random

WAGE_PER_HOUR = 20
HOUR_PER_DAY = 8
PART_TIME_HOUR = 4
TOTAL_HOURS = PART_TIME_HOUR + HOUR_PER_DAY
MAX_HOURS = 100
MAX_DAYS = 20
DAYS = 20

def daily_wages(wage, hour):
    total_wages = wage * hour
    print("Daily Wage is: ", total_wages)

def parttime_wage(wage, total):
    total_wages = wage * total
    print("Daily Wage is: ", total_wages)

def monthly_wage(wage, hours, days):
    monthly_wages = wage * hours * days
    print("Monthly Wage is: ", monthly_wages)

def check_attendance():
    TOTAL_HOURS_WORKED = 0
    TOTAL_DAYS_WORKED = 0
    while TOTAL_HOURS_WORKED < MAX_HOURS and TOTAL_DAYS_WORKED < MAX_DAYS:
        attendance_chk = random.randint(0,2)
        match attendance_chk:
            case 1:
                print("Employee is present for full time")
                TOTAL_DAYS_WORKED += 1
                TOTAL_HOURS_WORKED += HOUR_PER_DAY
                daily_wages(WAGE_PER_HOUR, HOUR_PER_DAY)
            case 2:
                print("Employee is present but for part-time")
                TOTAL_DAYS_WORKED += 1
                TOTAL_HOURS_WORKED += PART_TIME_HOUR
                daily_wages(WAGE_PER_HOUR, PART_TIME_HOUR)
            case _:
                print("Employee is absent")
                TOTAL_DAYS_WORKED += 1
                TOTAL_HOURS_WORKED += 0
    monthly_wage(WAGE_PER_HOUR, TOTAL_HOURS_WORKED, TOTAL_DAYS_WORKED)
check_attendance()

 
