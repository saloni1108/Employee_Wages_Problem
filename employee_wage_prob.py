import random

def check_attendance():
    attendance_chk = random.randint(0,1)
    if attendance_chk == 1:
        print("Employee is present")
    else:
        print("Employee is absent")
check_attendance()