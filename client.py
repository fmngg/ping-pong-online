import pygame
from network import Network
from ball import Ball

# font settings
pygame.font.init()
basic_font = pygame.font.Font('FreeSansBold.ttf', 32)
# screen settings
screen_width = 1280
playground_height = 720
screen_height = 800
win = pygame.display.set_mode((screen_width, screen_height))
# ball settings
ball = Ball(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30, (220, 20, 60))
# window name
pygame.display.set_caption("Client")


# all background objects
def surface_objects(pt, p2t):
    pygame.draw.aaline(win, (200, 200, 200), (screen_width / 2, 0), (screen_width / 2, screen_height))
    pygame.draw.rect(win, (176, 196, 222), (0, 0, 10, screen_height))
    pygame.draw.rect(win, (176, 196, 222), (screen_width - 10, 0, 10, screen_height))
    pygame.draw.rect(win, (176, 196, 222), (0, playground_height, screen_width, 10))
    pygame.draw.rect(win, (176, 196, 222), (0, screen_height - 10, screen_width, 10))
    pygame.draw.rect(win, (176, 196, 222), (0, 0, screen_width, 10))
    win.blit(pt, (660, 740))
    win.blit(p2t, (600, 740))
    ball.draw(win)


# screen updating
def redraw_window(win, player, player2, pt, p2t):
    win.fill('grey12')
    player.draw(win)
    player2.draw(win)
    surface_objects(pt, p2t)
    pygame.display.update()


# game
def main():
    # game variables
    run = True
    n = Network()
    p = n.get_p()
    clock = pygame.time.Clock()
    check_ready = False
    score_1 = 0
    score_2 = 0
    # game loop
    while run:
        clock.tick(60)  # frame rate
        p2 = n.send(p)
        player_text = basic_font.render(f'{score_1}', False, (200, 200, 200))  # score p1
        player2_text = basic_font.render(f'{score_2}', False, (200, 200, 200))  # score p2
        # quit loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()  # racket movement
        # starts the game if player 1 starts move
        if win.get_at((20, int(playground_height / 2 - 64))) == (70, 130, 180) or \
                win.get_at((20, int(playground_height / 2 + 64))) == (70, 130, 180) or check_ready:  # movement check
            check_ready = True
            ball.move()  # starts ball move
        # score update
        if ball.x <= 10:
            score_1 += 1
        if ball.x - 30 >= 1210:
            score_2 += 1
        redraw_window(win, p, p2, player_text, player2_text)  # screen update


# starts the game
main()
