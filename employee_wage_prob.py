import random

WAGE_PER_HOUR = 20
HOUR_PER_DAY = 8
PART_TIME_HOUR = 4

def daily_wages(wage, hour):
    total_wages = wage * hour
    print(total_wages)

def parttime_wage(wage, part_time_hour):
    total_wages = wage * part_time_hour
    print(total_wages)

def check_attendance():
    attendance_chk = random.randint(0,2)
    if attendance_chk == 1:
        print("Employee is present for full time")
        daily_wages(WAGE_PER_HOUR, HOUR_PER_DAY)
    elif attendance_chk == 2:
        print("employee is present but worked pat-time")
        parttime_wage(WAGE_PER_HOUR, PART_TIME_HOUR)
    else:
        print("Employee is absent")
check_attendance()
