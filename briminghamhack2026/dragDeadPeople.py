import pygame as py

class Drag:
    def __init__(self, group):
        self.group = group

    def dragSprite(self, p):
        for entity in self.group.sprites():
            # Only start dragging if the click happened INSIDE the square
            if entity.rect.collidepoint((p[0]-entity.position[0],p[1]-entity.position[1])):
                entity.isDragging = True
                break  # Prevents dragging multiple overlapping squares

    def dropSprite(self):
        for entity in self.group:
            entity.isDragging = False


