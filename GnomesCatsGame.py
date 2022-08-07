#!/usr/bin/env python3
# Here are we start again!
from game_classes import *


def main():
    pygame.init()
    # Define constants for the screen width and height

    player_1 = Player()

    # Create groups to hold enemy sprites and all sprites

    # - enemies is used for collision detection and position updates

    # - all_sprites is used for rendering

    enemies = pygame.sprite.Group()

    all_sprites = pygame.sprite.Group()

    all_sprites.add(player_1)

    screen = pygame.display.set_mode([screen_width, screen_height])

    # Create a custom event for adding a new enemy

    ADDENEMY = pygame.USEREVENT + 1

    pygame.time.set_timer(ADDENEMY, 250)

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

                all_sprites.add(new_enemy)

        # Get all the keys currently pressed

        pressed_keys = pygame.key.get_pressed()

        # Update the player sprite based on user keypresses

        player_1.update(pressed_keys)

        # Update enemy position

        enemies.update()

        screen.fill((0, 0, 255))

        pygame.draw.circle(screen, (255, 200, 255), (250, 250), 100)

        surf = pygame.Surface((50, 50))

        surf.fill((0, 0, 0))

        # Draw all sprites

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # Check if any enemies have collided with the player

        if pygame.sprite.spritecollideany(player_1, enemies):
            # If so, then remove the player and stop the loop

            player_1.kill()

            game_on = False

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
