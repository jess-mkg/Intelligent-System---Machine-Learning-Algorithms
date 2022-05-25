
from imports import math, np

#DISTANCE CALCULATION METHODS#
    
def chi_distance(rowA, rowB):                                   
    distance = 0.0       
    distance = 0.5 * np.sum([((a - b) ** 2) / (a + b) 
    for (a, b) in zip(rowA, rowB)])
    return math.sqrt(distance)
    

def cosine_distance(rowA, rowB):                                 
    distance = 0.0 
    dot = sum(a*b for a,b in zip(rowA, rowB))
    v1 =sum(a*a for a in rowA) ** 0.5
    v2 =sum(b*b for b in rowB) ** 0.5
    distance = 1 - dot/(v1*v2)
    return distance


def euclidean_distance(rowA, rowB):                              
    distance = 0.0                                                    
    for i in range(len(rowA)-1):
        distance += (rowA[i] - rowB[i])**2
    return math.sqrt(distance)


def manhattan_distance(rowA, rowB):
    distance = 0.0
    distance = sum(abs(a-b) for a,b in zip(rowA, rowB))
    return distance