# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 06:35:52 2020

@author: srees
"""

import random
import numpy as np
from numpy.random import choice
from collections import Counter 
import pandas as pd
class GeneticEngineering:
  def __init__(self,mutationRate,totalPopulation,crossOver,generationCount):
   self.mutationRate = mutationRate
   self.totalPopulation = totalPopulation
   self.crossOver = crossOver
   self.fitnessScore=0
   self.populationData = []
   self.fitnessData = []
   self.generationCount=generationCount
   self.alpha_list=[0,1,2,3,4,5,6,7]
  def create_initial_population(self):
    self.secure_random = random.SystemRandom()
    for outloop in range(self.totalPopulation):
      randomData = []
      fitnessScore = 0
      for inloop in range(len(self.alpha_list)):
        selectedData = self.secure_random.choice(self.alpha_list)
        randomData.append(selectedData)
      self.fitnessScore=self.getFitnessScore(randomData)
      self.populationData.append(randomData)
      self.fitnessData.append(self.fitnessScore)
      probabilityDist = []
      probDataFrame = pd.DataFrame({'String':self.populationData,'FitnessScore':self.fitnessData})
      probDataFrame = probDataFrame.sort_values(['FitnessScore'],ascending=False)
      probDataFrame = probDataFrame.reset_index(drop=True)
    return probDataFrame
  def print_solution(self):
    finalsequence = self.sequence[(self.sequence['FitnessScore']==28)] 
    print(finalsequence)  
  def getFitnessScore(self,data):
    '''
    The maximum possible clahses is 28. (14 row +columns and 14 diagoinal clases )
    '''
    clashes=0
    rwclashes=len(data) - len(np.unique(data))
    clashes+=rwclashes
    for i in range(len(data)):
      for j in range(len(data)):
        if (i!=j):
          dx = abs(i-j)
          dy=abs(data[i]-data[j])
          if (dx==dy):
            clashes+=1
    fitnessScore = 28 - clashes
    return fitnessScore
  def process_mutation(self,probDataFrame):
    self.solved=False
    crossOverPoint = 4
    print(crossOverPoint)
    print(self.generationCount)
    for loop in range(self.generationCount):
     draw=[]
     draw.append(probDataFrame[0:1]["String"].values[0])
     draw.append(probDataFrame[1:2]["String"].values[0])
      #print('Fitness Scores of Parents ',getFitnessScore(draw[0]),getFitnessScore(draw[1]))
     if (self.getFitnessScore(draw[0])==28| self.getFitnessScore(draw[1])==28):
       self.sequence=pd.DataFrame({'Solution':draw[0:2],'FitnessScore':[self.getFitnessScore(draw[0]),self.getFitnessScore(draw[1])]})
       print("solution", draw[0],' ',draw[1])
       self.solved=True
       break
     child1 = draw[0][0:crossOverPoint]+draw[1][crossOverPoint:]
     child2 = draw[1][0:crossOverPoint]+draw[0][crossOverPoint:]
     child1[random.randint(0,7)] =  self.secure_random.choice(self.alpha_list)
     child2[random.randint(0,7)] =  self.secure_random.choice(self.alpha_list)
     self.populationData.append(child1)
     self.populationData.append(child2)
     self.fitnessData = []
     self.totalPopulation = len(self.populationData)
     for outloop in range(self.totalPopulation):
       self.fitnessScore = self.getFitnessScore(self.populationData[outloop])
       self.fitnessData.append(self.fitnessScore)
     probabilityDist = []
     probDataFrame = pd.DataFrame({'String':self.populationData,'FitnessScore':self.fitnessData})
     probDataFrame = probDataFrame.sort_values(['FitnessScore'],ascending=False)
     probDataFrame = probDataFrame.reset_index(drop=True)
     print('Generation ','Average Fitness Score ',probDataFrame["FitnessScore"].mean(),'child1:',probDataFrame[0:1]["String"].values[0],'child2:',probDataFrame[1:2]["String"].values[0])
  #print('Generation ',loop,' ',' Average Fitness Score ',probDataFrame["FitnessScore"].mean())
    return self.solved 

if (__name__ == '__main__'):
 ge=GeneticEngineering(.01,150,0.5,1200)
 pd1=ge.create_initial_population()
 pd1.head()
 solution=ge.process_mutation(pd1)
 if (solution == True):
  ge.print_solution()
else:
 print("repeat the generation to solve the equation")  
  
