import time

import pygame
import numpy as np
import Brain
import MovementEquations
from Entity import Entity
from enum import Enum



segs = [72,48,22,0]

class LookDir(Enum):
    lookFront = 0
    lookRight = 1
    lookBack = 2
    lookLeft = 3

class DeadPerson(Entity):
    def constructDirs(self):
        #side
        sideHat = pygame.image.load("Assets/Sprites/Characters/Hats/Hat1Side.png").convert_alpha()
        sideHead = pygame.image.load("Assets/Sprites/Characters/Heads/SkullSide.png").convert_alpha()
        sideSprite1 = [pygame.image.load("Assets/Sprites/Characters/Pants/Pants1Side1.png").convert_alpha(),
                       pygame.image.load("Assets/Sprites/Characters/Shirts/Shirt1Side1.png").convert_alpha(),
                       sideHead,
                       sideHat]

        sideSprite2 = [pygame.image.load("Assets/Sprites/Characters/Pants/Pants1Side2.png").convert_alpha(),
                       pygame.image.load("Assets/Sprites/Characters/Shirts/Shirt1Side2.png").convert_alpha(),
                       sideHead,
                       sideHat]

        sideSprite3 = [pygame.image.load("Assets/Sprites/Characters/Pants/Pants1Side3.png").convert_alpha(),
                       pygame.image.load("Assets/Sprites/Characters/Shirts/Shirt1Side3.png").convert_alpha(),
                       sideHead,
                       sideHat]

        sideSurface1 = pygame.Surface((self.spriteWidth,self.spriteHeight), pygame.SRCALPHA)
        for i in range(len(segs)):
            sideSurface1.blit(sideSprite1[i], pygame.rect.Rect(0, segs[i], self.spriteWidth, self.spriteWidth))
        sideSurface2 = pygame.Surface((self.spriteWidth, self.spriteHeight), pygame.SRCALPHA)
        for i in range(len(segs)):
            sideSurface2.blit(sideSprite2[i], pygame.rect.Rect(0, segs[i], self.spriteWidth, self.spriteWidth))
        sideSurface3 = pygame.Surface((self.spriteWidth, self.spriteHeight), pygame.SRCALPHA)
        for i in range(len(segs)):
            sideSurface3.blit(sideSprite3[i], pygame.rect.Rect(0, segs[i], self.spriteWidth, self.spriteWidth))

        # Front
        frontHat = pygame.image.load("Assets/Sprites/Characters/Hats/Hat1Front.png").convert_alpha()
        frontHead = pygame.image.load("Assets/Sprites/Characters/Heads/SkullFront.png").convert_alpha()
        frontSprite1 = [pygame.image.load("Assets/Sprites/Characters/Pants/Pants1Front1.png").convert_alpha(),
                       pygame.image.load("Assets/Sprites/Characters/Shirts/Shirt1Front1.png").convert_alpha(),
                       frontHead,
                       frontHat]

        frontSprite2 = [pygame.image.load("Assets/Sprites/Characters/Pants/Pants1Front2.png").convert_alpha(),
                       pygame.image.load("Assets/Sprites/Characters/Shirts/Shirt1Front2.png").convert_alpha(),
                       frontHead,
                       frontHat]

        frontSprite3 = [pygame.image.load("Assets/Sprites/Characters/Pants/Pants1Front3.png").convert_alpha(),
                       pygame.image.load("Assets/Sprites/Characters/Shirts/Shirt1Front3.png").convert_alpha(),
                       frontHead,
                       frontHat]

        frontSurface1 = pygame.Surface((self.spriteWidth, self.spriteHeight), pygame.SRCALPHA)
        for i in range(len(segs)):
            frontSurface1.blit(frontSprite1[i], pygame.rect.Rect(0, segs[i], self.spriteWidth, self.spriteWidth))
        frontSurface2 = pygame.Surface((self.spriteWidth, self.spriteHeight), pygame.SRCALPHA)
        for i in range(len(segs)):
            frontSurface2.blit(frontSprite2[i], pygame.rect.Rect(0, segs[i], self.spriteWidth, self.spriteWidth))
        frontSurface3 = pygame.Surface((self.spriteWidth, self.spriteHeight), pygame.SRCALPHA)
        for i in range(len(segs)):
            frontSurface3.blit(frontSprite3[i], pygame.rect.Rect(0, segs[i], self.spriteWidth, self.spriteWidth))

        # back
        backHead = pygame.image.load("Assets/Sprites/Characters/Heads/SkullBack.png").convert_alpha()
        backSprite1 = [pygame.image.load("Assets/Sprites/Characters/Pants/Pants1Back1.png").convert_alpha(),
                        pygame.image.load("Assets/Sprites/Characters/Shirts/Shirt1Back1.png").convert_alpha(),
                        backHead,
                        frontHat]

        backSprite2 = [pygame.image.load("Assets/Sprites/Characters/Pants/Pants1Back2.png").convert_alpha(),
                        pygame.image.load("Assets/Sprites/Characters/Shirts/Shirt1Back2.png").convert_alpha(),
                        backHead,
                        frontHat]

        backSprite3 = [pygame.image.load("Assets/Sprites/Characters/Pants/Pants1Back3.png").convert_alpha(),
                        pygame.image.load("Assets/Sprites/Characters/Shirts/Shirt1Back3.png").convert_alpha(),
                        backHead,
                        frontHat]

        backSurface1 = pygame.Surface((self.spriteWidth, self.spriteHeight), pygame.SRCALPHA)
        for i in range(len(segs)):
            backSurface1.blit(backSprite1[i], pygame.rect.Rect(0, segs[i], self.spriteWidth, self.spriteWidth))
        backSurface2 = pygame.Surface((self.spriteWidth, self.spriteHeight), pygame.SRCALPHA)
        for i in range(len(segs)):
            backSurface2.blit(backSprite2[i], pygame.rect.Rect(0, segs[i], self.spriteWidth, self.spriteWidth))
        backSurface3 = pygame.Surface((self.spriteWidth, self.spriteHeight), pygame.SRCALPHA)
        for i in range(len(segs)):
            backSurface3.blit(backSprite3[i], pygame.rect.Rect(0, segs[i], self.spriteWidth, self.spriteWidth))

        return [sideSurface1,sideSurface2,sideSurface3], [frontSurface1,frontSurface2,frontSurface3], [backSurface1,backSurface2,backSurface3]

    def __init__(self, name: str,speed: int, zoomFactor: int, sprites: list, position: list = [0,0,0]):

        self.spriteHeight = 96
        self.spriteWidth = 32

        sprites = [pygame.Surface((self.spriteWidth,self.spriteHeight))]
        self.name = name
        super().__init__(speed, zoomFactor, sprites, position)


        self.isDragging = False
        self.lookDir = LookDir.lookFront
        self.curFrame = 0

        self.slowAni = 5
        self.tick = 0


        self.displayName = False

        self.sideAnims, self.frontAnims, self.backAnims = self.constructDirs()
        self.animArray = [self.frontAnims, self.sideAnims, self.backAnims]

        self.image = self.frontAnims[self.curFrame]



        self.brain = Brain.brain(300,1600, 400,700)
        self.controller = MovementEquations.MovementEquations(np.array([960,-1228.8]))

    def setImage(self, surface):
        self.holdImage = surface

    def changeDir(self, lookDir):
        self.lookDir = lookDir
        self.curFrame = 0
        if lookDir.value == 0:
            self.sprites = self.frontAnims
            self.setImage(self.frontAnims[0])
        elif lookDir.value == 1 or lookDir.value == 3:
            self.sprites = self.sideAnims
            self.setImage(self.sideAnims[0])
        else:
            self.sprites = self.backAnims
            self.setImage(self.backAnims[0])

    def nextFrame(self):
        self.curFrame += 1
        tVal = self.lookDir.value
        if tVal == 3:
            tVal = 1
        if self.curFrame >= len(self.animArray[tVal]):
            self.curFrame = 0

        self.setImage(self.animArray[tVal][self.curFrame])


    def getDisplayName(self, screen) -> pygame.Surface:
        f = pygame.font.SysFont(pygame.font.get_default_font(),size=round(16*self.zoomFactor))
        s=pygame.font.Font.render(f, self.name, 1, "red")
        return s


    def update(self, dt):
        if self.isDragging:
            self.position = [pygame.mouse.get_pos()[0] - (self.spriteWidth // 2),
                             pygame.mouse.get_pos()[1] - (self.spriteHeight // 2)]
            self.brain.hasTarget = False
        else:
            if self.tick >= self.slowAni:
                self.nextFrame()
                self.tick = 0
            else:
                self.tick+=1

        if not self.brain.hasTarget:
            self.brain.generatePoint()
            print(self.brain.target)
        else:
            # posVect = np.array([self.position[0],self.position[1]])
            dir = (self.brain.target[0]-self.position[0],self.brain.target[1]-self.position[1])
            nextPos = (self.position[0]+dir[0]*dt*self.speed,self.position[1]+dir[1]*dt*self.speed)
            if nextPos == self.position:
                self.brain.hasTarget = False
            else:
                self.position = nextPos


        if self.position[1] < 327:
            self.position = (self.position[0],327)

        if self.position[1] > 720:
            self.position = (self.position[0], 720)

        if self.position[0] < 205 + 225*((723-self.position[1])/345):
            self.position = (205 + 225*((723-self.position[1])/345), self.position[1])

        if self.position[0] > 1604 - 187*((709-self.position[1])/327):
            self.position = (1604 - 187*((709-self.position[1])/327), self.position[1])

        d = (547 - self.position[1])/533
        self.zoomFactor = (1- (0.5)*d) * 3.33

        self.image = pygame.transform.scale_by(self.holdImage, self.zoomFactor)
        self.rect = self.image.get_rect()
