import sys
import pygame
import pygame_gui


def start_mainmenu():
    from DungeonMaster import start_map
    f = open('Fullscreen.txt', mode='r')
    Fullscreen = bool(int(f.read()))
    f.close()
    pygame.init()
    pygame.display.set_caption('Dungeon Master')
    if Fullscreen:
        size1 = ScreenWidth, ScreenHeight = pygame.display.Info().current_w, \
                                            pygame.display.Info().current_h
        screen = pygame.display.set_mode(size1, pygame.FULLSCREEN)
    else:
        size1 = ScreenWidth, ScreenHeight = 900, 700
        screen = pygame.display.set_mode(size1)
    Font = pygame.font.SysFont('Liberation Serif', 100)
    text = Font.render('Dungeon Master', False, (255, 255, 255))
    text_rect = pygame.Rect(ScreenWidth//2-340, 60, 800, 200)
    screen.blit(text, text_rect)

    manager = pygame_gui.UIManager((ScreenWidth, ScreenHeight))

    StartGame = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
        (ScreenWidth // 2 - 100, ScreenHeight // 2+80), (200, 50)),
        text='Start game', manager=manager)
    StatisticsButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
        (ScreenWidth // 2 - 100, ScreenHeight // 2 + 160), (200, 50)),
        text='Statistics', manager=manager)
    ExitButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
        (ScreenWidth // 2 - 100, ScreenHeight // 2 + 240), (200, 50)),
        text='Exit', manager=manager)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == StatisticsButton:
                    pass
                elif event.ui_element == StartGame:
                    start_map()
                elif event.ui_element == ExitButton:
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    DisplaySize = pygame.display.get_window_size()
                    pygame.quit()
                    pygame.init()
                    pygame.display.set_caption('Dungeon Master')
                    if DisplaySize == (900, 700):
                        size = ScreenWidth, ScreenHeight = pygame.display.Info().current_w, \
                                                           pygame.display.Info().current_h
                        screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
                        f = open('Fullscreen.txt', mode='w')
                        f.write('1')
                        f.close()
                    else:
                        size = ScreenWidth, ScreenHeight = 900, 700
                        screen = pygame.display.set_mode(size)
                        f = open('Fullscreen.txt', mode='w')
                        f.write('0')
                        f.close()
                    StartGame.kill()
                    StatisticsButton.kill()
                    ExitButton.kill()
                    manager = pygame_gui.UIManager((ScreenWidth, ScreenHeight))
                    StartGame = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                        (ScreenWidth // 2 - 100, ScreenHeight // 2 + 80), (200, 50)),
                        text='Start game', manager=manager)
                    StatisticsButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                        (ScreenWidth // 2 - 100, ScreenHeight // 2 + 160), (200, 50)),
                        text='Statistics', manager=manager)
                    ExitButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                        (ScreenWidth // 2 - 100, ScreenHeight // 2 + 240), (200, 50)),
                        text='Exit', manager=manager)

            manager.process_events(event)

        manager.update(clock.tick(60))

        manager.draw_ui(screen)

        pygame.display.update()
