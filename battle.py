import random
import sys
import sqlite3

import pygame
from infobattle import Info
from unit import Unit, Boss
from items import Consumable_items, items_Sword, items_BodyArmor, items_Gloves, items_Greaves, \
    items_Ring, items_Helmet


def start_battle(flag):
    from DungeonMaster import start_map
    from FinalScreen import FinalScreen
    hero_anim_breathing = ["image/hero_anim/hero_battle_anim_breathing_1.png",
                           "image/hero_anim/hero_battle_anim_breathing_2.png",
                           "image/hero_anim/hero_battle_anim_breathing_3.png",
                           "image/hero_anim/hero_battle_anim_breathing_2.png"]

    enemy_anim_breathing = ["image/enemy_anim/enemy.png",
                            "image/enemy_anim/enemy_2.png",
                            "image/enemy_anim/enemy_3.png",
                            "image/enemy_anim/enemy_2.png"]

    boss_anim_breathing = ["image/boss_anim/boss_anim_1.png",
                           "image/boss_anim/boss_anim_2.png",
                           "image/boss_anim/boss_anim_3.png",
                           "image/boss_anim/boss_anim_4.png"]

    icons = [pygame.image.load("image/icons/attack.png"),
             pygame.image.load("image/icons/shild.png"),
             pygame.image.load("image/icons/potion.png"),
             pygame.image.load("image/icons/fireball.png"),
             pygame.image.load("image/icons/poison.png")]

    def render(screen, hero, enemy):
        screen.blit(icons[0], (AttackPosX, 500))
        screen.blit(icons[1], (DefendPosX, 500))
        screen.blit(icons[2], (HealingPosX, 500))
        screen.blit(icons[3], (ConsumableItemPosX, 500))
        all_sprites.update(ArtPosX)
        all_sprites.draw(screen)
        window_status(hero, enemy)
        info.render()
        if hero.anim.flag_window_hp:
            hero.window_hp()
        if enemy.anim.flag_window_hp:
            enemy.window_hp()

    def window_status(hero, enemy):
        myfont = pygame.font.SysFont('Liberation Serif', 30)
        # hp hero
        text = myfont.render(str(hero.hp), False, (255, 255, 255))
        text_rect = pygame.Rect(ArtPosX + 150, 20, 30, 30)
        screen.blit(text, text_rect)

        # hp enemy
        text = myfont.render(str(enemy.hp), False, (255, 255, 255))
        text_rect = pygame.Rect(ArtPosX + 640, 20, 30, 30)
        screen.blit(text, text_rect)

        # count potion
        tfont = pygame.font.SysFont('Liberation Serif', 100)
        text = tfont.render(str(hero.count_potion), False, [155, 155, 0, 128])
        rect = text.get_rect(center=(HealingPosX + 50, 550))
        rect_surf = pygame.Surface((1225, 700), pygame.SRCALPHA)
        rect_surf.blit(text, rect)
        screen.blit(rect_surf, (0, 0),  special_flags=pygame.BLEND_MAX)

        # recharge healing
        if hero.recharge_healing != 0:
            text = myfont.render(str(hero.recharge_healing), False, (255, 255, 255))
            text_rect = pygame.Rect(HealingPosX, 470, 30, 30)
            screen.blit(text, text_rect)

        # recharge Consumable items
        if hero.recharge_Consumable_items != 0:
            text = myfont.render(str(hero.recharge_Consumable_items), False, (255, 255, 255))
            text_rect = pygame.Rect(ConsumableItemPosX, 470, 30, 30)
            screen.blit(text, text_rect)

        myfont = pygame.font.SysFont('Liberation Serif', 20)
        # poison
        if hero.poison_move > 0:
            screen.blit(icons[4], (ArtPosX + 365, 50))
            text = myfont.render(str(hero.poison_move), False, (255, 255, 255))
            rect = text.get_rect(center=(ArtPosX + 390, 40))
            screen.blit(text, rect)

        if enemy.poison_move > 0:
            screen.blit(icons[4], (ArtPosX + 440, 50))
            text = myfont.render(str(enemy.poison_move), False, (255, 255, 255))
            rect = text.get_rect(center=(ArtPosX + 465, 40))
            screen.blit(text, rect)

    def get_button(pos):
        x = int(pos[0])
        y = int(pos[1])
        if 500 <= y <= 600 and not flag_inventory:
            if AttackPosX <= x <= AttackPosX + 100:
                return 1
            elif DefendPosX <= x <= DefendPosX + 100:
                return 2
            elif HealingPosX <= x <= HealingPosX + 100:
                return 3
            elif ConsumableItemPosX <= x <= ConsumableItemPosX + 100:
                return 4
        if ScreenHeight - 150 <= y <= ScreenHeight - 50:
            if 25 <= x <= 325:
                return 8
        return None

    def attack(self, other):
        dm = self.attack(other, True)
        other.taking_damage(dm)

    pygame.init()
    pygame.display.set_caption('Dungeon Master')
    size = ScreenWidth, ScreenHeight = 1225, 700
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()

    dop_x = 150
    AttackPosX = ScreenWidth // 2 - 350 + dop_x
    DefendPosX = ScreenWidth // 2 - 150 + dop_x
    HealingPosX = ScreenWidth // 2 + 50 + dop_x
    ConsumableItemPosX = ScreenWidth // 2 + 250 + dop_x

    ArtPosX = ScreenWidth // 2 - 425 + dop_x
    f = open('ReceivedArtefacts.txt', mode='r')
    arr_Artefacts = f.readline().split("/")
    f.close()
    hero = Unit(0, hero_anim_breathing, ArtPosX, 50, 'hero', screen, all_sprites)
    f = open('HeroClothes.txt', mode='r')
    hero.putting_on_clothes(f.read().split('\n'))
    f.close()
    f = open('ReceivedClothes.txt', mode='r')
    Received_clothes = f.read().split('\n')
    f.close()
    f = open('StatisticsPerGame.txt', mode='r')
    KilledEnemies, AllReceived_clothes, AllReceived_artefacts = list(map(int, f.read().split()))
    f.close()
    if Received_clothes == [""]:
        Received_clothes = []
    hero.putting_artefacts(arr_Artefacts)
    hero.putting_on_consumable_items("fireball")
    f = open('Hero.txt', mode='r')
    n = f.read().split()
    hero.hp = float(n[0])
    hero.set_count_potion(int(n[1]))
    f.close()
    # enemy = 0, boss = 1
    if flag == 0:
        f = open('mob_progression.txt', mode='r')
        lv = int(f.read())
        f.close()
        enemy = Unit(lv, enemy_anim_breathing, ArtPosX, 50, 'enemy', screen, all_sprites)
        enemy.putting_on_clothes(["", "", "", "", "", ""])
    elif flag == 1:
        enemy = Boss(15, boss_anim_breathing, ArtPosX, 50, 'enemy', screen, all_sprites)
        enemy.putting_on_clothes(["", "", "", "", "", ""])
    f = open('ContinueBattle.txt', mode='r')
    ContinueBattle = bool(int(f.read()))
    f.close()
    f = open('lastAccount.txt', mode='r')
    LastAccount, Login = f.read().split('\n')
    f.close()
    if ContinueBattle:
        f = open('Enemy.txt', mode='r')
        enemy.hp = float(f.read())
        f.close()
        f = open('EnemyStatusEffects.txt', mode='r')
        Poison = f.read().split()
        enemy.poison_move = int(Poison[0])
        enemy.poison_dm = int(Poison[1])
        f.close()
        f = open('EnemyClothes.txt', mode='r')
        enemy.putting_on_clothes(f.read().split('\n'))
        f.close()
        f = open('HeroStatusEffects.txt', mode='r')
        Poison = f.read().split()
        hero.poison_move = int(Poison[0])
        hero.poison_dm = int(Poison[1])
        f.close()
        f = open('Cooldowns.txt', mode='r')
        hero.recharge_healing, hero.recharge_Consumable_items = list(map(int, f.read().split()))
        f.close()

    info = Info(screen, ScreenWidth, ScreenHeight, 10, 10, hero, enemy)
    pattern_atk_enemy = [1, 1, 2, 1, 2, 1, 1, 2, 2, 1]
    flag_atk_enemy = 0

    fps = 30
    clock = pygame.time.Clock()
    running = True
    flag_move = True
    flag_enemy_move = False
    flag_inventory = False
    flag_anim = False
    time_anim = 30
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('Continue.txt', mode='w')
                f.write('1')
                f.close()
                f = open('ContinueBattle.txt', mode='w')
                f.write('1')
                f.close()
                f = open('Enemy.txt', mode='w')
                f.write(str(enemy.hp))
                f.close()
                f = open('EnemyStatusEffects.txt', mode='w')
                f.write(str(enemy.poison_move) + ' ' + str(enemy.poison_dm))
                f.close()
                f = open('EnemyClothes.txt', mode='w')
                f.write('\n'.join(enemy.items))
                f.close()
                f = open('Hero.txt', mode='w')
                f.write(str(hero.hp) + ' ' + str(hero.get_count_potion()))
                f.close()
                f = open('HeroStatusEffects.txt', mode='w')
                f.write(str(hero.poison_move) + ' ' + str(hero.poison_dm))
                f.close()
                f = open('Cooldowns.txt', mode='w')
                f.write(str(hero.recharge_healing) + ' ' + str(hero.recharge_Consumable_items))
                f.close()
                f = open('lastAccount.txt', mode='w')
                f.write(Login + '\n' + Login)
                f.close()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                if flag_inventory:
                    button = info.button_inventory(event.pos)
                    if button != None and button != 8:
                        info.render_info(button)
                else:
                    button = get_button(event.pos)
                    if button != None and button != 8:
                        info.render_info(button)
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
                                if hero.recharge_healing == 0 and hero.count_potion > 0:
                                    hero.healing()
                                    flag_move = False
                                    flag_anim = True
                            elif button == 4:
                                if hero.recharge_Consumable_items == 0:
                                    enemy.taking_damage(hero.use_consumable_items())
                                    flag_move = False
                                    flag_anim = True
                            elif button == 8:
                                info.render_info(button)
                                flag_inventory = not flag_inventory
                            else:
                                flag_move = True
                                flag_anim = False
        if not flag_move and enemy.status() and not flag_anim:
            if flag_atk_enemy > len(pattern_atk_enemy) - 1:
                flag_atk_enemy = 0
            if pattern_atk_enemy[flag_atk_enemy] == 1:
                attack(enemy, hero)
            else:
                enemy.defense()
            flag_anim = True
            flag_enemy_move = True
            flag_atk_enemy += 1
        if not enemy.status() and not flag_anim:
            pygame.quit()
            f = open('Continue.txt', mode='w')
            f.write('1')
            f.close()
            f = open('MapNumber.txt', mode='r')
            NumberOfRooms, RoomNumber = list(map(int, f.read().split()))
            f.close()
            f = open('ContinueBattle.txt', mode='w')
            f.write('0')
            f.close()
            f = open('Hero.txt', mode='w')
            f.write(str(hero.hp) + ' ' + str(enemy.poison_dm))
            f.close()
            i = 'default'
            while i == 'default':
                i = random.choice([random.choice(list(items_Sword.keys())),
                                   random.choice(list(items_BodyArmor.keys())),
                                   random.choice(list(items_Gloves.keys())),
                                   random.choice(list(items_Greaves.keys())),
                                   random.choice(list(items_Helmet.keys())),
                                   random.choice(list(items_Ring.keys()))])
            if len(Received_clothes) < 12:
                Received_clothes.append(i)
            else:
                Received_clothes[0] = i
            f = open('ReceivedClothes.txt', mode='w')
            f.write('\n'.join(Received_clothes))
            f.close()
            AccFile = sqlite3.connect('accounts.sqlite3')
            AccFileInf = AccFile.cursor()
            AccFileInf.execute("""UPDATE accounts
                                    SET KilledEnemies = KilledEnemies + 1
                                WHERE Login = ?""", (Login,))

            KilledEnemies += 1
            AllReceived_clothes += 1
            f = open('StatisticsPerGame.txt', mode='w')
            f.write(str(KilledEnemies) + ' ' + str(AllReceived_clothes) + ' ' + str(AllReceived_artefacts))
            f.close()
            if RoomNumber == NumberOfRooms:
                pygame.quit()
                f = open('Continue.txt', mode='w')
                f.write('0')
                f.close()
                AccFileInf.execute("""UPDATE accounts
                                        SET Wins = Wins + 1
                                      WHERE Login = ?""", (Login,))
                AccFile.commit()
                AccFile.close()
                FinalScreen(True, KilledEnemies, AllReceived_clothes, AllReceived_artefacts)
            else:
                running = False
                AccFile.commit()
                AccFile.close()
                start_map()
        elif not hero.status() and not flag_anim:
            pygame.quit()
            f = open('Continue.txt', mode='w')
            f.write('0')
            f.close()
            f = open('ContinueBattle.txt', mode='w')
            f.write('0')
            f.close()
            AccFile = sqlite3.connect('accounts.sqlite3')
            AccFileInf = AccFile.cursor()
            AccFileInf.execute("""UPDATE accounts
                                        SET Loses = Loses + 1
                                    WHERE Login = ?""", (Login,))
            AccFile.commit()
            AccFile.close()
            running = False
            FinalScreen(False, KilledEnemies, AllReceived_clothes, AllReceived_artefacts)
        render(screen, hero, enemy)
        clock.tick(fps)
        if flag_anim:
            time_anim -= 1
            if time_anim == 0:
                time_anim = 30
                flag_anim = False
                if flag_enemy_move:
                    hero.time_motion()
                    enemy.time_motion()
                    flag_move = True
                    flag_enemy_move = False
        pygame.display.flip()
