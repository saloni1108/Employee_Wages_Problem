import random

WAGE_PER_HOUR = 20
HOUR_PER_DAY = 8
PART_TIME_HOUR = 4
TOTAL_HOURS = PART_TIME_HOUR + HOUR_PER_DAY
MAX_HOURS = 100
MAX_DAYS = 20
DAYS = 20
DAILY_WAGE = []
TOTAL_WAGE = []

def daily_wages(wage, hour):
    total_wages = wage * hour
    DAILY_WAGE.append(total_wages)
    return total_wages

def parttime_wage(wage, total):
    total_wages = wage * total
    DAILY_WAGE.append(total_wages)
    return total_wages

def monthly_wage(wage, hours, days):
    monthly_wages = wage * hours * days
    TOTAL_WAGE.append(monthly_wages)
    return monthly_wages

def check_attendance():
    TOTAL_HOURS_WORKED = 0
    TOTAL_DAYS_WORKED = 0
    while TOTAL_HOURS_WORKED < MAX_HOURS and TOTAL_DAYS_WORKED < MAX_DAYS:
        attendance_chk = random.randint(0,2)
        match attendance_chk:
            case 1:
                print("Employee is present")
                daily_wages(WAGE_PER_HOUR, HOUR_PER_DAY)
                TOTAL_HOURS_WORKED += HOUR_PER_DAY
                TOTAL_DAYS_WORKED += 1
                monthly_wage(WAGE_PER_HOUR, TOTAL_HOURS_WORKED, TOTAL_DAYS_WORKED)
            case 2:
                print("Employee is present")
                parttime_wage(WAGE_PER_HOUR, TOTAL_HOURS)
                TOTAL_HOURS_WORKED += TOTAL_HOURS
                TOTAL_DAYS_WORKED += 1
                monthly_wage(WAGE_PER_HOUR, TOTAL_HOURS_WORKED, TOTAL_DAYS_WORKED)
            case _:
                print("Employee is absent")
    total_working_hours(TOTAL_HOURS_WORKED)
    print("Daily Wage is: ", DAILY_WAGE)
    print("Total Wage is: ", TOTAL_WAGE)
def total_working_hours(hours):
    print("total hour: ", hours)

check_attendance()
 
