import pygame
import random

screen_width = 1280
screen_height = 720
win = pygame.display.set_mode((screen_width, screen_height))


class Ball:
    def __init__(self, x, y, width, height, color):  # ball settings
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.speed_x = 7 * random.choice((-1, 1))
        self.speed_y = 7 * random.choice((-1, 1))

    def draw(self, win):  # draw a ball
        pygame.draw.ellipse(win, self.color, self.rect)

    def move(self):  # ball movement
        self.x += self.speed_x
        self.y += self.speed_y

        if self.y <= 10 or self.y >= screen_height - 40:
            self.speed_y *= -1
        if self.x <= 10 or self.x >= screen_width - 40:
            self.speed_x *= -1
        self.check_pixel()
        self.update()

    def update(self):  # ball update
        self.rect = (self.x, self.y, self.width, self.height)

    def check_pixel(self):  # check collisions
        pixel_ml = win.get_at((int(self.x) - 5, int(self.y) + 15))
        pixel_mr = win.get_at((int(self.x) + 30, int(self.y) + 15))
        pixel_tl = win.get_at((int(self.x) - 5, int(self.y)))
        pixel_tr = win.get_at((int(self.x) + 30, int(self.y)))
        pixel_bl = win.get_at((int(self.x) - 5, int(self.y) + 30))
        pixel_br = win.get_at((int(self.x) + 30, int(self.y) + 30))

        if pixel_ml == (70, 130, 180) or pixel_tl == (70, 130, 180) or pixel_bl == (70, 130, 180):
            self.speed_x *= -1
        if pixel_mr == (200, 200, 200) or pixel_tr == (200, 200, 200) or pixel_br == (200, 200, 200):
            self.speed_x *= -1
