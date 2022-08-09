#!/usr/bin/env python3
# Here are we start again!
import time

import pygame.sprite

from game_classes import *


def main():

    pygame.mixer.init()

    pygame.init()
    clock = pygame.time.Clock()

    pygame.mixer.music.load("sprites/Naruto_Theme.mp3")

    pygame.mixer.music.play(loops=-1)

    move_up_sound = pygame.mixer.Sound("sprites/jumping.wav")

    move_down_sound = pygame.mixer.Sound("sprites/jumping.wav")

    collision_sound = pygame.mixer.Sound("sprites/hit.wav")

    enemies = pygame.sprite.Group()

    clouds = pygame.sprite.Group()
    # Define constants for the screen width and height
    screen = pygame.display.set_mode([screen_width, screen_height])
    player_1 = Player(move_up_sound, move_down_sound)

    all_sprites_upper = pygame.sprite.Group()
    all_sprites_lower = pygame.sprite.Group()

    # all_sprites.add(player_1)

    # Create a custom event for adding a new enemy

    ADDENEMY = pygame.USEREVENT + 1

    pygame.time.set_timer(ADDENEMY, 250)

    ADDECLOUD = pygame.USEREVENT + 2

    pygame.time.set_timer(ADDECLOUD, 1000)

    game_on = True
    while game_on:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_on = False

            elif event.type == pygame.QUIT:
                game_on = False

            elif event.type == ADDENEMY:
                # Create the new enemy and add it to sprite groups

                new_enemy = Enemy()

                enemies.add(new_enemy)

                all_sprites_upper.add(new_enemy)

            elif event.type == ADDECLOUD:
                # Create the new enemy and add it to sprite groups

                new_cloud = Cloud()

                clouds.add(new_cloud)

                if random.randint(0, 3) == 0:
                    all_sprites_upper.add(new_cloud)
                else:
                    all_sprites_lower.add(new_cloud)

        # Get all the keys currently pressed

        pressed_keys = pygame.key.get_pressed()

        # Update the player sprite based on user keypresses

        player_1.update(pressed_keys)

        # Update enemy position

        enemies.update()
        clouds.update()

        screen.fill((135, 206, 250))

        # Draw all sprites

        for entity in all_sprites_lower:
            screen.blit(entity.surf, entity.rect)

        screen.blit(player_1.surf, player_1.rect)

        for entity in all_sprites_upper:
            screen.blit(entity.surf, entity.rect)




        # Check if any enemies have collided with the player

        if pygame.sprite.spritecollideany(player_1, enemies):
            # If so, then remove the player and stop the loop

            player_1.kill()
            move_up_sound.stop()

            move_down_sound.stop()

            collision_sound.play()

            time.sleep(1)

            game_on = False

        pygame.display.flip()
        clock.tick(30)

    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()

    # Ensure program maintains a rate of 30 frames per second


if __name__ == "__main__":
    main()
