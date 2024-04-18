import random

def check_attendance():
    n = random.randint(0,1)
    if n == 1:
        print("Employee is present")
    else:
        print("Employee is absent")
check_attendance()

wage_per_hour = 20
hour_per_day = 8
def daily_wages(w, h):
    wages = w * h
    print(wages)
daily_wages(wage_per_hour, hour_per_day)