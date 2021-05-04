import pygame

screen_width = 1280
screen_height = 720


class Player:
    def __init__(self, x, y, width, height, color):  # player settings
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.speed = 6

    def draw(self, win):  # draw player
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):  # player movement
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

    def update(self):  # player update
        self.rect = (self.x, self.y, self.width, self.height)