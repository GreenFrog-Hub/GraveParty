from Entity import Entity
from Type import Type

class Object(Entity):
    def __init__(self, name, zoomFactor: int, sprites: list, position: list = [0,0,0]):
        super().__init__(0, zoomFactor, type, sprites, position)
        self.type = Type(name.upper())

    def getType(self):
        return self.type

