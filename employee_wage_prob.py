import random

def check_attendance():
    n = random.randint(0,1)
    if n == 1:
        print("Employee is present")
    else:
        print("Employee is absent")
check_attendance()