import pygame
from network import Network

screen_width = 1280
screen_height = 720
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Client")

clientNum = 0


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.speed = 6

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if self.y <= 10:
            self.y = 10
        if self.y >= screen_height - 136:
            self.y = screen_height - 136

        if keys[pygame.K_UP]:
            self.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.y += self.speed

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

'''
class Ball:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.speed_x = 7
        self.speed_y = 7

    def draw(self, win):
        pygame.draw.ellipse(win, self.color, self.rect)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.y <= 0 or self.y >= screen_height:
            self.speed_y *= -1
        if self.x <= 0 or self.x >= screen_width:
            self.speed_x *= -1

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
'''


def read_pos(str):
    str = str.split(",")
    return int(float(str[0])), int(float(str[1]))


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redraw_window(win, player, player2): #ball):
    win.fill('grey12')
    player.draw(win)
    player2.draw(win)
    #ball.draw(win)
    pygame.draw.aaline(win, (200, 200, 200), (screen_width / 2, 0), (screen_width / 2, screen_height))
    pygame.display.update()


def main():
    run = True
    n = Network()
    startPos = read_pos(n.get_pos())
    p = Player(startPos[0], startPos[1], 10, 126, (70, 130, 180))
    p2 = Player(0, 0, 10, 126, (200, 200, 200))
    #ball = Ball(screen_width / 2, screen_height / 2, 50, 50, (205, 92, 92))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        #ballPos = read_pos(n.send(make_pos((ball.x, ball.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        #ball.x = ballPos[0]
        #ball.y = ballPos[1]
        p2.update()
        #ball.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        #ball.move()
        redraw_window(win, p, p2) #, ball)


main()
