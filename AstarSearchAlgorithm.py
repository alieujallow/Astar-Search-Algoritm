#!/usr/bin/env python3
from ev3dev.ev3 import *
from library import *
from Map import *
from queue import*
from math import* 
from Node import* 




#a method that initializes the map
def initializeMap(worldMap):
  for i in range(ROW_SIZE):
    for j in range(COLUMN_SIZE):
      val = worldMap[i][j]
      worldMap[i][j] = Node()
      if(val==1):
        worldMap[i][j].setWalkable(False)
      if(start[0]==i and start[1]==j):
        worldMap[i][j].setG(0)
        
        
        
        
#a method that prints the map with the F values     
def printing(worldMap):
  for i in range(ROW_SIZE):
    for j in range(COLUMN_SIZE):
      print("("+str(worldMap[i][j].getF())+")",end=" ")
    print()
    print()
    
    
    
    
#a method that checks if a cell is valid
def isValid(world_map,cell):
  if(world_map[cell[0]][cell[1]].isWalkable()):
    return True
  return False 
  
  
  
   
#a method that gets the distance between two nodes
def getDistanceBetweenTwoCells(currentCell,goalCell):
  col = abs(currentCell[1] - goalCell[1])
  row = abs(currentCell[0] - goalCell[0])
  
  if(col>row):
    return (DIAGONAL_MOVEVEMENT_COST*row + ORTHOGONAL_MOVEVEMENT_COST*(col-row))
  return (DIAGONAL_MOVEVEMENT_COST*col + ORTHOGONAL_MOVEVEMENT_COST*(row-col))
  
  
  
  
#a method that retraces the shortest path
def getShortestPath(startCell,goalCell):
  #creates a list
  shortestPath  = []
  currentCell = goalCell
  while True: 
    #checks if current cell is equal to goal cell
    if(currentCell[0]==startCell[0] and currentCell[1]==startCell[1]):
      break
    shortestPath.append(currentCell)
    currentCell = world_map[currentCell[0]][currentCell[1]].getParent()
  shortestPath.append(startCell)
  return  shortestPath  
  
  
  
    
#a method that takes in the current location as a tuple and returns a list of its neighboring cells
def getNeighbouringCells(currentLocation):
  row = currentLocation[0]
  column = currentLocation[1]
  neighboringCells = []
  
  #checks if the values of the tuple are valid
  if((row>=0 and row<ROW_SIZE) and (column>=0 and column<COLUMN_SIZE)):
  
    #checking whether the current cell has a cell to its left
    if((column-1)>=0):
      neighboringCells.append((row,column-1))
      
    #checking whether the current cell has a cell to its right
    if((column+1)<COLUMN_SIZE):
      neighboringCells.append((row,column+1))
      
    #checking whether the current cell has an upper cell
    if((row-1)>=0):
      neighboringCells.append((row-1,column))
      
    #checking whether the current cell has a cell below it
    if((row+1)<ROW_SIZE):
      neighboringCells.append((row+1,column)) 
    
    #checking whether the current cell has a cell in up left diagonal
    if(row-1>=0 and column-1>=0):
      neighboringCells.append((row-1,column-1)) 
    
    #checking whether the current cell has a cell in up right diagonal
    if(row-1>=0 and column+1<COLUMN_SIZE):
      neighboringCells.append((row-1,column+1)) 
    
    #checking whether the current cell has a cell in down left diagonal
    if(row+1<ROW_SIZE and column-1>=0):
      neighboringCells.append((row+1,column-1)) 
    
    #checking whether the current cell has a cell in down right diagonal
    if(row+1<ROW_SIZE and column+1<COLUMN_SIZE):
      neighboringCells.append((row+1,column+1)) 
      
    return neighboringCells
  else:
    return neighboringCells
    
    
    
        
#a method that finds the shortes path
def findPath(start,goal):

  #creates an open list
  openedList = PriorityQueue()
  
  #creates a closed list
  closedList = []
  
  #adds the start node to the opened list
  startCell=(0,start)
  openedList.put(startCell)
  
  #starts a while loop
  while not openedList.empty():
  
    #gets the cell with the lowest f value
    currentCell  = openedList.get()
    currentCell  = currentCell[1]
     
    #adds the current cell to the closed list
    closedList.append(currentCell)
    
    
    #checks if the current node is the goal node
    if(goal[0]==currentCell[0] and goal[1]==currentCell[1]):
      return getShortestPath(start,goal)
      
    #gets the neighbors of the current node
    neighboringCells = getNeighbouringCells(currentCell)
    
    #looping through all the neighbors of the current cell
    for i in range(len(neighboringCells)):
      neighborCell = neighboringCells[i]
      neighbourNode = world_map[neighborCell[0]][neighborCell[1]]
      
      if(isValid(world_map,neighborCell)==False or neighborCell in closedList): #checks if the neighbor is not walkable or closed list contains neighbor
        continue
        
      newMovementCostToNeighbor = world_map[currentCell[0]][currentCell[1]].getG() + getDistanceBetweenTwoCells(currentCell,neighborCell)
      
      if(newMovementCostToNeighbor<neighbourNode.getG() or (not any(neighborCell in item for item in openedList.queue))):
        neighbourNode.setG(newMovementCostToNeighbor)
        neighbourNode.setH(getDistanceBetweenTwoCells(neighborCell,goal))
        neighbourNode.setParent(currentCell)

        if(not any(neighborCell in item for item in openedList.queue)):
          openedList.put((neighbourNode.getF(),neighborCell))
          
          
          
            
#a method that takes in the shortest path moves the robot from the start to the goal
def moveToGoal(shortestPath):
  
  #sets the start location as the current location
  currentCell  = shortestPath.pop()
  
  #sets the orientation of the robot
  currentCellOrientation = 1
  
  while(True):
  
    #checks if the current location is the same as the goal cell
    if(currentCell[0]==goal[0] and currentCell[1]==goal[1]):
      break
      
    #gets the next cell
    nextCell = shortestPath.pop()
    
    #gets the orientation of of the next cell
    nextCellOrientation = getOrientation(currentCell,nextCell)
    currentCell = nextCell
    
    #sets the movement distance
    if(nextCellOrientation == 8 or nextCellOrientation == 2 or nextCellOrientation == 4 or nextCellOrientation == 6 ):
      movementDistance = DIAGONAL_MOVEVEMENT_DISTANCE
    else:
      movementDistance = ORTHOGONAL_MOVEVEMENT_DISTANCE
    
    difference = nextCellOrientation - currentCellOrientation
    currentCellOrientation = nextCellOrientation
    
    #checks if the difference is less than 0
    if(difference<0):
      difference = abs(difference)
      turnLeft(difference*TURNING_ANGLE, TURNING_SPEED)
      moveStraight(movementDistance,MOVING_SPEED)
      stopMotor()
    else: 
      turnRight(difference*TURNING_ANGLE, TURNING_SPEED)
      moveStraight(movementDistance,MOVING_SPEED)
      stopMotor()
      
      
      
            
#a method that gets the orientation of the next cell in relation to the current cell
def getOrientation(currentCell,nextCell):
  
  #checks if the next cell is to the left of the current cell
  if(currentCell[0]==nextCell[0] and currentCell[1]>nextCell[1]):
    return 7
  
  #checks if the next cell is to the right of the current cell
  elif(currentCell[0]==nextCell[0] and currentCell[1]<nextCell[1]):
    return 3
 
  #checks if the next cell is at the top of the current cell
  elif(currentCell[0]>nextCell[0] and currentCell[1]==nextCell[1]):
    return 1
    
  #checks if the next cell is at the bottom of the current cell
  elif(currentCell[0]<nextCell[0] and currentCell[1]==nextCell[1]):
    return 5
 
  
  #checks if the next cell is at the top left of the current cell
  elif(currentCell[0]>nextCell[0] and currentCell[1]>nextCell[1]):
    return 8
    
  #checks if the next cell is at the top right of the current cell
  elif(currentCell[0]>nextCell[0] and currentCell[1]<nextCell[1]):
    return 2
  
  #checks if the next cell is at the bottom left of the current cell
  elif(currentCell[0]<nextCell[0] and currentCell[1]>nextCell[1]):
    return 6
    
  #checks if the next cell is at the bottom RIGHT of the current cell
  elif(currentCell[0]<nextCell[0] and currentCell[1]<nextCell[1]):
    return 4
    
    
    
    
#main method
def main(): 
  initializeMap(world_map)  
  shortestPath = findPath(start,goal)
  print(shortestPath)
  moveToGoal(shortestPath)
  
  
  
#calling the main method  
main()











