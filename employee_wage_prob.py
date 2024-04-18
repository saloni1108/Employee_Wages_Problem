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

part_time_hour = 4
total_hour = hour_per_day + part_time_hour
def parttime_wage(w, t):
    wages = w * t
    print(wages)
parttime_wage(wage_per_hour, total_hour)

options = {
    1: "Check employee attendance",
    2: "calculate dailiy wages",
    3: "calculate the wages after adding part-time",
    4: "invalid"
}

choose = int(input("Enter the case: "))
if choose == 1:
    check_attendance()
elif choose == 2:
    daily_wages(wage_per_hour, hour_per_day)
elif choose == 3:
    parttime_wage(wage_per_hour, total_hour)
else:
    print("invalid")

