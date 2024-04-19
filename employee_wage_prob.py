import random

def check_attendance():
    attendance_chk = random.randint(0,2)
    if attendance_chk == 1:
        print("Employee is present for full day")
    else:
        print("Employee is absent")
check_attendance()