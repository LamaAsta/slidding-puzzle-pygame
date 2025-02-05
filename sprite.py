import pygame
from settings import *

pygame.font.init()



class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text,dim,surface = 20):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.dim = dim
        self.game = game
        self.image = pygame.Surface(self.dim[::-1])
        self.x, self.y = x, y
        self.text = text
        self.rect = self.image.get_rect()
        if self.text != "empty":
            self.font = pygame.font.SysFont("Consolas", 50)
            self.image.fill(WHITE)
            self.font_size = self.font.size(self.text)
            self.image.blit(surface, (0,0))
        else:
            self.image.fill(BGCOLOUR)

    def update(self):
        self.rect.x = self.x * self.dim[1]
        self.rect.y = self.y * self.dim[0]

    def click(self, mouse_x, mouse_y):
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.bottom

    def right(self):
        return self.rect.x + self.dim[1] < GAME_SIZE * self.dim[1]

    def left(self):
        return self.rect.x - self.dim[1] >= 0

    def up(self):
        return self.rect.y - self.dim[0] >= 0

    def down(self):
        return self.rect.y + self.dim[0] < GAME_SIZE * self.dim[0]


class UIElement:
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text

    def draw(self, screen):
        font = pygame.font.SysFont("Consolas", 30)
        text = font.render(self.text, True, WHITE)
        screen.blit(text, (self.x, self.y))


class Button:
    def __init__(self, x, y, width, height, text, colour, text_colour):
        self.colour, self.text_colour = colour, text_colour
        self.width, self.height = width, height
        self.x, self.y = x, y
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("Consolas", 30)
        text = font.render(self.text, True, self.text_colour)
        self.font_size = font.size(self.text)
        draw_x = self.x + (self.width / 2) - self.font_size[0] / 2
        draw_y = self.y + (self.height / 2) - self.font_size[1] / 2
        screen.blit(text, (draw_x, draw_y))

    def click(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height
