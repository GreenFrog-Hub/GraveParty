import Entity

class Table(Entity):
    def __init__(self,sprites : list , position : list = [0,0,0]):
        super().__init__(0,1,sprites,position)
        self.snapPos1 = [position[0]+1,0,0]
        self.snapPos2 = [position[0]-1,0,0]