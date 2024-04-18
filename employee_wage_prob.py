import random

WAGE_PER_HOUR = 20
HOUR_PER_DAY = 8
PART_TIME_HOUR = 4
TOTAL_HOURS = PART_TIME_HOUR + HOUR_PER_DAY
DAYS = 20

def daily_wages(wage, hour):
    total_wages = wage * hour
    print(total_wages)

def parttime_wage(wage, total):
    total_wages = wage * total
    print(total_wages)

def monthly_wage(wage, hours, days):
    monthly_wages = wage * hours * days
    print(monthly_wages)

def check_attendance():
    attendance_chk = random.randint(0,2)
    match attendance_chk:
        case 1:
            print("Employee is present")
            daily_wages(WAGE_PER_HOUR, HOUR_PER_DAY)
            monthly_wage(WAGE_PER_HOUR, HOUR_PER_DAY, DAYS)
        case 2: 
            print("Employee is present")
            parttime_wage(WAGE_PER_HOUR, TOTAL_HOURS)
            monthly_wage(WAGE_PER_HOUR, TOTAL_HOURS, DAYS)
        case _:
            print("Employee is absent")
check_attendance()
 
