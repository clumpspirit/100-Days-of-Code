# This code passes all test cases at
# https://reeborg.ca/

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Get the wall to your right
while wall_on_right() == False:
    if front_is_clear() == True:
        move()
    else:
        turn_left()

# Hug the right wall and go forward, otherwise turn left
while at_goal() == False:
    if right_is_clear() == True:
        turn_right()
        move()
    elif front_is_clear() == True:
        move()
    else:
        turn_left()
