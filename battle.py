import pygame
from unit import Unit


def render(screen, hero, enemy):
    pygame.draw.rect(screen, (0, 255, 0), (50, 50, 100, 300), width=0)
    pygame.draw.rect(screen, (255, 0, 0), (750, 50, 100, 300), width=0)

    pygame.draw.rect(screen, (0, 0, 255), (400, 500, 100, 100), width=0)
    pygame.draw.rect(screen, (0, 255, 255), (100, 500, 100, 100), width=0)
    pygame.draw.rect(screen, (255, 0, 255), (700, 500, 100, 100), width=0)

    window_hp(hero, enemy)


def window_hp(hero, enemy):
    myfont = pygame.font.SysFont('Liberation Serif', 30)
    text = myfont.render(str(hero.hp), False, (255, 255, 255))
    text_rect = pygame.Rect(50, 20, 30, 30)
    screen.blit(text, text_rect)

    text = myfont.render(str(enemy.hp), False, (255, 255, 255))
    text_rect = pygame.Rect(750, 20, 30, 30)
    screen.blit(text, text_rect)


def get_button(pos):
    x = int(pos[0])
    y = int(pos[1])
    if 500 <= y <= 600:
        if 100 <= x <= 200:
            return 1
        if 400 <= x <= 500:
            return 2
        if 700 <= x <= 800:
            return 3
    return None


def attack(self, other):
    dm = self.attack(other)
    other.taking_damage(dm)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Dungeon Master')
    size = ScreenWidth, ScreenHeight = 900, 700
    screen = pygame.display.set_mode(size)
    hero = Unit(0)
    enemy = Unit(1)

fps = 10
clock = pygame.time.Clock()
running = True
flag_move = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if flag_move:
                if event.button == 1:
                    button = get_button(event.pos)
                    if button == 1:
                        attack(hero, enemy)
                        flag_move = False
    if not flag_move:
        attack(enemy, hero)
        flag_move = True
    render(screen, hero, enemy)
    clock.tick(fps)
    pygame.display.flip()
