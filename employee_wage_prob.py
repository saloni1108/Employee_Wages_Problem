import random

WAGE_PER_HOUR = 20
HOUR_PER_DAY = 8
PART_TIME_HOUR = 4
DAYS = 20

def daily_wages(wage, hour):
    total_wages = wage * hour
    print("Daily Wage is :", total_wages)

def parttime_wage(wage, part_time_hour):
    total_wages = wage * part_time_hour
    print("Daily Wage is: ", total_wages)

def monthly_wage(wage, hours, days):
    monthly_wages = wage * hours * days
    print("Monthly Wage is: ", monthly_wages)

def check_attendance():
    global WORKING_DAYS
    WORKING_DAYS = 1
    while WORKING_DAYS <=DAYS: 
        attendance_chk = random.randint(0,2)
        match attendance_chk:
            case 1:
                print("Employee is present for full day")
                daily_wages(WAGE_PER_HOUR, HOUR_PER_DAY)
                monthly_wage(WAGE_PER_HOUR, HOUR_PER_DAY, DAYS)
            case 2: 
                print("Employee is present but part-time")
                parttime_wage(WAGE_PER_HOUR, PART_TIME_HOUR)
                monthly_wage(WAGE_PER_HOUR, PART_TIME_HOUR, DAYS)
            case _:
                print("Employee is absent")
        WORKING_DAYS += 1


check_attendance()

