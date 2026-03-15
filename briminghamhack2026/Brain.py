import random

class brain:
    def __init__(self,xmin,xmax,ymin,ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.hasTarget = False
        self.target = None

    def generatePoint(self):
        position = [random.randint(self.xmin,self.xmax),
                    random.randint(self.ymin,self.ymax), 0]
        self.target = (position[0], position[1])
        self.hasTarget = True

