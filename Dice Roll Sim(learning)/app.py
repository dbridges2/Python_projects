#Import Numpy library
import numpy as np
#Import matplotlib.pyplot Library
import matplotlib.pyplot as plt

tosses = 100 #Number of tosses
prob = .5 #Probability of getting heads

simToss = np.random.choice(["Heads", "Tails"], size=tosses, p= [prob, 1 - prob])

#print(simToss)
#tosses == Heads creates a Boolean array and np.sum() counts how many trues there are
headsCount = np.sum(simToss == "Heads")#counts how many times Heads comes up
tailsCount = np.sum(simToss == "Tails")#counts how many times Tails comes up

print(headsCount)
print(tailsCount / tosses)