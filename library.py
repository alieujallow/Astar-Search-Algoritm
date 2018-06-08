#!/usr/bin/env python3
#
#@Authors :Abdul-Razak Adam, Alieu Jallow
#Library of functionalities for our robot

import ev3dev.ev3 as ev3

#Moves the robot in a straight line for a specified distance(cm) at a specific speed
#distance
#speed: 

b=12.3
r=3
c= 17.2
dist=50.24
rotation=360

def moveStraight(distance, speed):
  rightMotor = ev3.LargeMotor('outC')
  leftMotor = ev3.LargeMotor('outB')
  n = (rotation * distance) / c
  rightMotor.run_to_rel_pos(position_sp=n, speed_sp=speed)
  leftMotor.run_to_rel_pos(position_sp=n, speed_sp=speed)
  rightMotor.wait_while('running')
  leftMotor.wait_while('running')
  
def moveForever(speed):
  rightMotor = ev3.LargeMotor('outC')
  leftMotor = ev3.LargeMotor('outB')
  rightMotor.run_forever(speed_sp=speed)
  leftMotor.run_forever(speed_sp=speed)
  
def stopMotor():
  rightMotor = ev3.LargeMotor('outC')
  leftMotor = ev3.LargeMotor('outB')
  rightMotor.stop()
  leftMotor.stop()
  
  
#turns the robot to angle at a particular speed to the left
#angle:
#speed: 
def turnLeft(angle, speed):
  rightMotor = ev3.LargeMotor('outC')
  leftMotor = ev3.LargeMotor('outB')
  n = (b*angle)/r
  #leftMotor.stop()
  rightMotor.run_to_rel_pos(position_sp=n, speed_sp=speed)
  leftMotor.stop()
  rightMotor.wait_while('running')
  
  
#turns the robot to angle at a particular speed to the right
#angle:
#speed:
def turnRight(angle, speed):
  rightMotor = ev3.LargeMotor('outC')
  leftMotor = ev3.LargeMotor('outB')
  n = (b*angle)/r
  #rightMotor.stop()
  leftMotor.run_to_rel_pos(position_sp=n, speed_sp=speed)
  rightMotor.stop()
  leftMotor.wait_while('running')
  
#spin the robot to angle at a particular speed to the left
#angle:
#speed:
def spinLeft(angle, speed):
  rightMotor = ev3.LargeMotor('outC')
  leftMotor = ev3.LargeMotor('outB')
  d=(angle*dist)/rotation
  n = (rotation * d) / c
  rightMotor.run_to_rel_pos(position_sp=n, speed_sp=speed)
  leftMotor.run_to_rel_pos(position_sp=-n, speed_sp=speed)
  
  rightMotor.wait_while('running')
  leftMotor.wait_while('running')
  
#spin the robot to angle at a particular speed to the right
#angle:
#speed:
def spinRight(angle, speed):
  rightMotor = ev3.LargeMotor('outC')
  leftMotor = ev3.LargeMotor('outB')
  d=(angle*dist)/rotation
  n = (rotation * d) / c
  rightMotor.run_to_rel_pos(position_sp=n * -1, speed_sp=speed)
  leftMotor.run_to_rel_pos(position_sp=n, speed_sp=speed)
  rightMotor.wait_while('running')
  leftMotor.wait_while('running')



