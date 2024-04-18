import random


WAGE_PER_HOUR = 20
HOUR_PER_DAY = 8

def daily_wages(wage, hour):
    total_wages = wage * hour
    print(total_wages)

def check_attendance():
    attendance_chk = random.randint(0,2)
    if attendance_chk == 1:
        print("Employee is present")
        daily_wages(WAGE_PER_HOUR, HOUR_PER_DAY)
    else:
        print("Employee is absent")
check_attendance()



