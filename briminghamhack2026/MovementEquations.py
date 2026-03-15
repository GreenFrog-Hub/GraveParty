import math
import numpy as np
from token import FSTRING_START


class MovementEquations:
    def __init__(self, vanishingPoint):
        self.vanishingPoint = vanishingPoint
        self.basis = np.array([[0,0],[0,0]])


    def calcBasis(self, pos):
        self.xVect = np.array([1, 0])
        self.yVect = np.array([self.vanishingPoint[0] - pos[0], self.vanishingPoint[1] - pos[1]])
        self.modYVect = np.linalg.norm(self.yVect)
        self.yVect *= 1 / self.modYVect
        self.basis = np.array([self.xVect, self.yVect])

    def getBasisCoef(self, destination):
        b = destination[1] / ((1/self.modYVect)*(self.yVect[1]-self.yVect[0]))
        a = destination[0] - b*self.yVect
        return a,b

