#!/usr/bin/env python3
#
#@Author :Alieu Jallow
class Node:

   # contructor
   def __init__(self):
   
      self.g = 1000000
      self.h = 0
      self.f = 0
      self.parent =None
      self.walkable=True

   
   #getter metthods
   def getG(self):
     return self.g
     
   def getH(self):
     return self.h
     
   def getF(self):
     self.f =  self.g + self.h
     return self.f
   
   def isWalkable(self):
     return self.walkable
   
   def getParent(self):
     return self.parent
     
   #setter methods
   def setG(self,g):
     self.g = g
     
   def setH(self,h):
      self.h = h
   
   def setParent(self,parent):
     self.parent = parent
     
   def setWalkable(self,state):
     self.walkable=state
     
     
     
     
     