from pygame import sprite, Surface

class ExtendedGroup(sprite.LayeredUpdates):
    def draw(self, surface, fontSurface = None):
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            self.spritedict[spr] = surface_blit(spr.image, (spr.position[0], spr.position[1]))
            if spr.displayName:
                fontSurface = spr.getDisplayName(surface)
                a = surface_blit(fontSurface, (spr.position[0], spr.position[1]))

        self.lostsprites = []
