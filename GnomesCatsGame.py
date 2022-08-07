#!/usr/bin/env python3
# Here are we start again!
import pygame

from pygame.locals import (

    K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,

    KEYDOWN,

    QUIT,

)


def shutdown_func(game=True):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game = False

        elif event.type == pygame.QUIT:
            game = False

    return game


class Player(pygame.sprite.Sprite):

    def __init__(self, screenw, screenh):

        super(Player, self).__init__()

        self.surf = pygame.Surface((75, 25))

        self.surf.fill((255, 255, 255))

        self.rect = self.surf.get_rect()

        self.screenw = screenw
        self.screenh = screenh

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

        if self.rect.right > self.screenw:
            self.rect.right = self.screenw

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= self.screenh:
            self.rect.bottom = self.screenh


def main():
    pygame.init()
    # Define constants for the screen width and height

    SCREEN_WIDTH = 800

    SCREEN_HEIGHT = 600

    player_1 = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    game_on = True
    while game_on:

        game_on = shutdown_func()

        # Get all the keys currently pressed

        pressed_keys = pygame.key.get_pressed()

        # Update the player sprite based on user keypresses

        player_1.update(pressed_keys)

        screen.fill((0, 0, 255))

        pygame.draw.circle(screen, (255, 200, 255), (250, 250), 100)

        surf = pygame.Surface((50, 50))

        surf.fill((0, 0, 0))

        screen.blit(player_1.surf, player_1.rect)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
