import pygame
import random
import os

from pygame.locals import (

    K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,

    KEYDOWN,

    QUIT,

)

screen_width = int(os.getenv("SCREEN_WIDTH"))
screen_height = int(os.getenv("SCREEN_HEIGHT"))


def shutdown_func(game=True):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game = False

        elif event.type == pygame.QUIT:
            game = False

    return game


class Player(pygame.sprite.Sprite):

    def __init__(self):

        super(Player, self).__init__()

        self.surf = pygame.Surface((75, 25))

        self.surf.fill((255, 255, 255))

        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)

        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > screen_width:
            self.rect.right = screen_width

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()

        self.surf = pygame.Surface((20, 10))

        self.surf.fill((255, 255, 255))

        self.rect = self.surf.get_rect(

            center=(

                random.randint(screen_width + 20, screen_width + 100),

                random.randint(0, screen_height),

            )

        )

        # self.speed = random.randint(1, 2)
        self.speed = 1

    def update(self):
        self.rect.move_ip(-self.speed, 0)

        if self.rect.right < 0:
            self.kill()


