import os

import pygame

from Cursor import Cursor
from ExtendedGroup import ExtendedGroup
from dragDeadPeople import Drag


class GraveyardEnv:
    def __init__(self):
        pygame.init()
        displayMode = pygame.SRCALPHA | pygame.NOFRAME
        self.screen = pygame.display.set_mode((1920,1080), displayMode)
        self.screen.lock()
        self.clock = pygame.time.Clock()

        self.background=None

        self.objects = ExtendedGroup()
        self.deadPeople = ExtendedGroup()

        self.drag = Drag(self.deadPeople)

        self.hotspot = (0,0)
        # self.c = Cursor()
        pygame.mouse.set_visible(True)
        self.normalCursor = pygame.image.load(os.path.join("Assets", "Sprites", "Icons", "Mouse", "ScytheStable.png"))
        self.clickCursor = pygame.image.load(os.path.join("Assets", "Sprites", "Icons", "Mouse", "ScytheDown.png"))
        pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), self.normalCursor))



    def addObject(self, object):
        pygame.sprite.LayeredUpdates.add(self.objects, object)

    def addDeadPerson(self, deadPerson):
        pygame.sprite.LayeredUpdates.add(self.deadPeople, deadPerson)

    def drawObject(self):
        if len(pygame.sprite.LayeredUpdates.sprites(self.objects)) != 0:
            self.screen.unlock()
            pygame.sprite.LayeredUpdates.draw(self.objects, self.screen)
            self.screen.lock()

    def drawDeadPeople(self):
        if len(pygame.sprite.LayeredUpdates.sprites(self.deadPeople)) != 0:
            self.screen.unlock()
            ExtendedGroup.draw(self.deadPeople, self.screen)
            self.screen.lock()


    def setBackground(self, path:str):
        self.background = pygame.transform.scale_by(pygame.image.load(path),4.44)


    def drawBackground(self) -> bool:
        if self.background is not None:
            self.screen.unlock()
            self.screen.fill("black")
            pygame.Surface.blit(self.screen, self.background, (0,0))
            self.screen.lock()
            return True
        else:
            print("\nPLEASE SET A BACKGROUND\n")
            self.closeWindow()
            return False


    def startMainLoop(self):
        self.dt = 0
        running = True
        while running:
            running = self.mainLoop()

        self.closeWindow()

    def mainLoop(self) -> bool:
        e = pygame.event.get()
        # pygame.mouse.set_cursor(pygame.cursors.Cursor(self.hotspot, self.c.currentCursor(e)))
        for event in e:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), self.clickCursor))
                self.drag.dragSprite(event.pos)

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), self.normalCursor))
                self.drag.dropSprite()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False


        if not self.drawBackground():
            return False

        self.checkMouseHover()

        pygame.sprite.LayeredUpdates.update(self.deadPeople, dt = self.dt)
        pygame.sprite.LayeredUpdates.update(self.objects)

        self.moveLayer()
        self.drawObject()
        self.drawDeadPeople()

        pygame.display.flip()
        self.dt = self.clock.tick(60)/1000

        return True

    def checkMouseHover(self):
        p = pygame.mouse.get_pos()
        for entity in self.deadPeople.sprites():
            # Only start dragging if the click happened INSIDE the square
            if entity.rect.collidepoint((p[0]-entity.position[0],p[1]-entity.position[1])) or entity.isDragging:
                entity.displayName = True
                 # Prevents dragging multiple overlapping squares
            else:
                entity.displayName = False

    def moveLayer(self):
        for entity in self.deadPeople.sprites():
            pygame.sprite.LayeredUpdates.change_layer(self.deadPeople, entity, entity.calcLayer(entity.zoomFactor))
        for entity in self.objects.sprites():
            pygame.sprite.LayeredUpdates.change_layer(self.objects, entity, entity.calcLayer(entity.zoomFactor))



    def closeWindow(self):
        pygame.quit()
