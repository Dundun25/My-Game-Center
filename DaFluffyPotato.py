from pygame.locals import *


def run():
    import pygame
    # Initiation
    fps = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption("Gura Adventure")

    window_size = (1280, 720)
    screen = pygame.display.set_mode(window_size, 0, 32)
    display = pygame.Surface((300, 200))

    # maybe useful later : background = pygame.image.load("Resource/bg.jpg")
    # platform = pygame.image.load("Resource/map/dirtwithgrass.png")
    dirt = pygame.image.load("Resource/map/dirt.png")
    dirt = pygame.transform.scale(dirt, (18, 18))
    grass = pygame.image.load("Resource/map/kusagrass.png")
    grass = pygame.transform.scale(grass, (18, 18))
    tile_size = dirt.get_width()

    # Map Generator
    def map_generator(file_path):
        generated_map = open(file_path, "r")
        content = generated_map.read()
        generated_map.close()
        content = content.split()
        generated_map = []
        for row in content:
            generated_map.append(list(row))
        return generated_map

    custom_map = map_generator("Resource/map/map.txt")

    # Player init
    player = pygame.image.load("Resource/gura_crop.png")
    player = pygame.transform.scale(player, (player.get_width() // 12, player.get_height() // 12))
    player_rect = pygame.Rect(50, 50, player.get_width() - 8, player.get_height() - 2)
    player_y_momentum = 0
    right = False
    left = False
    up = False
    down = False
    jump = True
    air_timer = 0
    scroll = [0, 0]

    # Collision Function

    def collision(rect, tiles):
        collisions = []
        for tile in tiles:
            if rect.colliderect(tile):
                collisions.append(tile)
        return collisions

    def move(rect, movement, tiles):
        collision_type = {"top": False, "bottom": False, "left": False, "right": False}
        rect.x += movement[0]
        hit_list = collision(rect, tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_type["right"] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_type["left"] = True
        rect.y += movement[1]
        hit_list = collision(rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_type["bottom"] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_type["top"] = True

        return rect, collision_type

    while True:

        display.fill((0, 250, 250))
        scroll[0] += (player_rect.x - scroll[0] - 100) // 20
        scroll[1] += (player_rect.y - scroll[1] - 100) // 20
        tile_rect = []
        y = 0
        for row in custom_map:
            x = -1
            for tile in row:
                if tile == "1":
                    display.blit(dirt, (x * (tile_size - 2) - scroll[0], y * (tile_size - 2) - scroll[1]))
                    tile_rect.append(pygame.Rect(x * (tile_size - 2), y * (tile_size - 2), tile_size, tile_size))
                if tile == "2":
                    display.blit(grass, (x * (tile_size - 2) - scroll[0], y * (tile_size - 2) - scroll[1]))

                x += 1
            y += 1

        player_movement = [0, 0]
        if right:
            player_movement[0] += 2
        if left:
            player_movement[0] -= 2
        player_movement[1] = player_y_momentum
        player_y_momentum += 0.2
        if player_y_momentum > 5:
            player_y_momentum = 5

        player_rect, collisions = move(player_rect, player_movement, tile_rect)
        display.blit(player, (player_rect.x - scroll[0], player_rect.y - scroll[1]))

        if collisions["bottom"]:
            jump = False
            player_y_momentum = 1
            air_timer = 0
        else:
            jump = True
            air_timer += 1
        if collisions["top"]:
            player_y_momentum = 1

        # Event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                pygame.display.quit()
                return
            if event.type == KEYDOWN:
                if event.key == K_d:
                    right = True
                if event.key == K_a:
                    left = True
                if event.key == K_s:
                    down = True
                if event.key == K_w:
                    if air_timer < 10:
                        if not jump:
                            player_y_momentum -= 6
                        up = True

            if event.type == KEYUP:
                if event.key == K_d:
                    right = False
                if event.key == K_a:
                    left = False
                if event.key == K_s:
                    down = False
                if event.key == K_w:
                    up = False

        surf = pygame.transform.scale(display, window_size)
        screen.blit(surf, (0, 0))
        pygame.display.update()
        fps.tick(60)