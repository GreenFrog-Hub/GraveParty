
import pygame,os.path
class Cursor:
    def __init__(self):
        self.normalCursor = pygame.image.load(os.path.join("Assets","Sprites", "Icons", "Mouse", "ScytheStable.png"))
        self.clickCursor = pygame.image.load(os.path.join("Assets","Sprites", "Icons", "Mouse", "ScytheDown.png"))
        self.heldDown = False

    def currentCursor(self, a):
        for event in a:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("click down")
                return self.clickCursor
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                print("click up")
                return self.normalCursor
        return self.normalCursor




