import pygame
from unit import Unit


def start_battle():
    hero_anim_breathing = ["image/hero_anim/hero_battle_anim_breathing_1.png",
                           "image/hero_anim/hero_battle_anim_breathing_2.png",
                           "image/hero_anim/hero_battle_anim_breathing_3.png",
                           "image/hero_anim/hero_battle_anim_breathing_2.png"]

    def render(screen, hero, enemy):
        pygame.draw.rect(screen, (0, 255, 255), (100, 500, 100, 100), width=0)
        pygame.draw.rect(screen, (0, 0, 255), (300, 500, 100, 100), width=0)
        pygame.draw.rect(screen, (255, 0, 255), (500, 500, 100, 100), width=0)
        pygame.draw.rect(screen, (255, 255, 255), (700, 500, 100, 100), width=0)
        window_hp(hero, enemy)

    def window_hp(hero, enemy):
        myfont = pygame.font.SysFont('Liberation Serif', 30)
        # hp hero
        text = myfont.render(str(hero.hp), False, (255, 255, 255))
        text_rect = pygame.Rect(50, 20, 30, 30)
        screen.blit(text, text_rect)

        # hp enemy
        text = myfont.render(str(enemy.hp), False, (255, 255, 255))
        text_rect = pygame.Rect(750, 20, 30, 30)
        screen.blit(text, text_rect)

        # recharge_healing
        if hero.recharge_healing != 0:
            text = myfont.render(str(hero.recharge_healing), False, (255, 255, 255))
            text_rect = pygame.Rect(500, 470, 30, 30)
            screen.blit(text, text_rect)

        # recharge_Consumable_items
        if hero.recharge_Consumable_items != 0:
            text = myfont.render(str(hero.recharge_Consumable_items), False, (255, 255, 255))
            text_rect = pygame.Rect(700, 470, 30, 30)
            screen.blit(text, text_rect)

    def get_button(pos):
        x = int(pos[0])
        y = int(pos[1])
        if 500 <= y <= 600:
            if 100 <= x <= 200:
                return 1
            elif 300 <= x <= 400:
                return 2
            elif 500 <= x <= 600:
                return 3
            elif 700 <= x <= 800:
                return 4
        return None

    def attack(self, other):
        dm = self.attack(other)
        other.taking_damage(dm)

    f = open('Fullscreen.txt', mode='r')
    Fullscreen = bool(int(f.read()))
    f.close()
    pygame.init()
    pygame.display.set_caption('Dungeon Master')
    if Fullscreen:
        size = ScreenWidth, ScreenHeight = pygame.display.Info().current_w, \
                                           pygame.display.Info().current_h
        screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    else:
        size = ScreenWidth, ScreenHeight = 900, 700
        screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()

    AttackPosX = ScreenWidth // 2 - 350
    DefendPosX = ScreenWidth // 2 - 150
    HealingPosX = ScreenWidth // 2 + 50
    ConsumableItemPosX = ScreenWidth // 2 + 250
    PosY = 500

    ArtPosX = ScreenWidth // 2 - 400
    hero = Unit(0, hero_anim_breathing, ArtPosX, 50, 'hero', all_sprites)
    hero.putting_on_clothes(["fire sword", "rusty body armor", "fire gloves", "rusty greaves", "", "", ""])
    hero.putting_on_consumable_items("fireball")
    enemy = Unit(2, hero_anim_breathing, ArtPosX, 50, 'enemy', all_sprites)

    fps = 5
    clock = pygame.time.Clock()
    running = True
    flag_move = True
    flag_anim = False
    time_anim = 5
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if flag_move and not flag_anim:
                    if event.button == 1:
                        button = get_button(event.pos)
                        if hero.status():
                            if button == 1:
                                attack(hero, enemy)
                                flag_move = False
                                flag_anim = True
                            elif button == 2:
                                hero.defense()
                                flag_move = False
                                flag_anim = True
                            elif button == 3:
                                if hero.recharge_healing == 0:
                                    hero.healing(50)
                                    flag_move = False
                                    flag_anim = True
                            elif button == 4:
                                if hero.recharge_Consumable_items == 0:
                                    enemy.taking_damage(hero.use_consumable_items())
                                    flag_move = False
                                    flag_anim = True
                            else:
                                flag_move = True
                                flag_anim = False
        if not flag_move and enemy.status() and not flag_anim:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    DisplaySize = pygame.display.get_window_size()
                    pygame.quit()
                    pygame.init()
                    pygame.display.set_caption('Dungeon Master')
                    f = open('Fullscreen.txt', mode='w')
                    if DisplaySize == (900, 700):
                        size = ScreenWidth, ScreenHeight = pygame.display.Info().current_w, \
                                                           pygame.display.Info().current_h
                        screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
                        f.write('1')
                    else:
                        size = ScreenWidth, ScreenHeight = 900, 700
                        screen = pygame.display.set_mode(size)
                        f = open('Fullscreen.txt', mode='w')
                        f.write('0')
                    f.close()
                    AttackPosX = ScreenWidth // 2 - 350
                    DefendPosX = ScreenWidth // 2 - 150
                    HealingPosX = ScreenWidth // 2 + 50
                    ConsumableItemPosX = ScreenWidth // 2 + 250
                    ArtPosX = ScreenWidth // 2 - 400
        if not flag_move and enemy.status() and not flag_anim:
            attack(enemy, hero)
            flag_move = True
            hero.time_motion()
            enemy.time_motion()
        if not hero.status() or not enemy.status():
            pygame.quit()
            f = open('Continue.txt', mode='w')
            f.write('1')
            f.close()
            from DungeonMaster import start_map
            start_map()
        elif not hero.status():
            pygame.quit()
            f = open('Continue.txt', mode='w')
            f.write('0')
            f.close()
            from DungeonMaster import start_map
            start_map()
        render(screen, hero, enemy)
        all_sprites.update(ArtPosX)
        all_sprites.draw(screen)
        clock.tick(fps)
        if flag_anim:
            time_anim -= 1
            if time_anim == 0:
                time_anim = 5
                flag_anim = False
        pygame.display.flip()
