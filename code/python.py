myVariable = 0

def when_started1():
    global myVariable
    for repeat_count in range(3):
        drivetrain.drive_for(FORWARD, 350, MM)
        arm5.spin_for(FORWARD, 120, DEGREES)
        claw.spin_for(FORWARD, 100, DEGREES)
        drivetrain.drive_for(REVERSE, 400, MM)
        drivetrain.turn_for(RIGHT, 200, DEGREES)
        drivetrain.drive_for(FORWARD, 400, MM)
        arm5.spin_for(REVERSE, 120, DEGREES)
        claw.spin_for(REVERSE, 100, DEGREES)
        drivetrain.drive_for(REVERSE, 400, MM)
        drivetrain.turn_for(RIGHT, 150, DEGREES)
        wait(5, MSEC)

when_started1()
