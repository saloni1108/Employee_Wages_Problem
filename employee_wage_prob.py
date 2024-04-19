import random

WAGE_PER_HOUR = 20
HOUR_PER_DAY = 8
PART_TIME_HOUR = 4


def daily_wages(wage, hour):
    total_wages = wage * hour
    print("Daily Wage is :", total_wages)

def parttime_wage(wage, part_time_hour):
    total_wages = wage * part_time_hour
    print("Daily Wage is: ", total_wages)

def check_attendance():
    attendance_chk = random.randint(0,2)
    match attendance_chk:
        case 1:
            print("Employee is present for full day")
            daily_wages(WAGE_PER_HOUR, HOUR_PER_DAY)
        case 2: 
            print("Employee is present but part-time")
            parttime_wage(WAGE_PER_HOUR, PART_TIME_HOUR)
        case _:
            print("Employee is absent")
check_attendance()

