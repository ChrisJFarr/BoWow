## Standardizing movement of robot to a finite set of functions
## Rotate: int input for degrees to turn
## Drive: boolean forward input for direction and int distance for inches to drive


# todo Syncing commands with robot_drive (permanent version of robot drive arduino code)
# todo On initizializing, set default speed with
# data.write(struct.pack('>B', default_speed))

# todo Drive robot forward for x seconds and measure distance traveled
# Full speed
# Half speed

# todo Rotate robot for x seconds and calculate degrees rotated
# todo change speed and calculate again, try to predict movement for any speed assuming linear variations



# Use keyboard control for driving robot
# import serial
# Linux
from robot_drive import RobotDrive
import argparse



##rd = RobotDrive()

# Program the planning parser
# Take a plan using a default speed, parse and perform actions

##plan = "flfffrfffrfff"
##for move in list(plan):

##actions = rd.actions()

##for action in plan:
##    actions[action]()


# Planning algorithms

# Breadth first search

# Create representation for 4 x 5 grid, top right starting square
rows = 4
columns = 5
grid = [[0 for r in range(rows)] for c in range(columns)]
starting_location = (0, 4)
def set_obstacle(loc):
    grid[loc[0]][loc[1]] = "-"
def set_goal(loc):
    grid[loc[0]][loc[1]] = 1
    
# Obstacle 1
obs1 = (0, 2)
set_obstacle(obs1)
# Obstacle 2
obs2 = (1, 2)
set_obstacle(obs2)
# Obstacle 3
obs3 = (2, 2)
set_obstacle(obs3)
# Set goal
goal = (0, 0)
set_goal(goal)

# Represent obstacles and easily adapt
# Create function for printing grid
grid_print = ""
for c in grid:
    i = 0
    for r in c:
        i += 1
        square = "| " + str(r) + " "
        if i >= len(c):
            square += "\n"
        grid_print += square

print(grid_print)


# Create functions for moving player through world










