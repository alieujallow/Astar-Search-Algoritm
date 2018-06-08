#!/usr/bin/env python3
#
#@Author :Alieu Jallow

#global variables
COLUMN_SIZE = 5
ROW_SIZE = 4

FREE = 0
OBST = 1

MOVING_SPEED  = 210
TURNING_SPEED  = 100

ORTHOGONAL_MOVEVEMENT_DISTANCE  = 45
DIAGONAL_MOVEVEMENT_DISTANCE  = 60

TURNING_ANGLE = 45

DIAGONAL_MOVEVEMENT_COST = 14
ORTHOGONAL_MOVEVEMENT_COST = 10

world_map =   [[1,0, 0, 1, 0],
		          [0, 0, 0, 0, 0],
		          [0, 1, 1, 1, 0],
		          [0, 0, 1, 0, 0]]   


#start and goal cells             
start= (3,0)
goal = (3,4)
