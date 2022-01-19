import sys
import pygame
import pygame_gui


def FinalScreen(Win, Killed, Items, Artefacts):
    from MainMenu import start_mainmenu
    from DungeonMaster import start_map
    pygame.init()
    pygame.display.set_caption('Dungeon Master')
    size = ScreenWidth, ScreenHeight = 1225, 700
    screen = pygame.display.set_mode(size)

    def Create_text(size):
        if Win:
            Font = pygame.font.SysFont('Liberation Serif', size)
            text = Font.render('You Win', False, (0, 255, 0))
        else:
            Font = pygame.font.SysFont('Liberation Serif', size)
            text = Font.render('You Lose', False, (255, 0, 0))
        return text

    def Create_text2(size, textvalue):
        Font = pygame.font.SysFont('Liberation Serif', size)
        text = Font.render(textvalue, False, (255, 255, 255))
        return text

    text = Create_text(100)
    text_rect = pygame.Rect(ScreenWidth // 2 - 190, 60, 500, 200)
    screen.blit(text, text_rect)
    text2 = Create_text2(30, f'You killed {Killed} enemies, collect {Items}'
                             f' items and {Artefacts} artefacts.')
    text_rect2 = pygame.Rect(ScreenWidth // 2 - 320, 170, 500, 200)
    screen.blit(text2, text_rect2)

    manager = pygame_gui.UIManager((ScreenWidth, ScreenHeight))
    MainMenu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
        (ScreenWidth // 2 - 110, ScreenHeight // 2 + 80), (220, 50)),
        text='Return to the main menu', manager=manager)
    Restart = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
        (ScreenWidth // 2 - 110, ScreenHeight // 2 + 160), (220, 50)),
        text='Restart', manager=manager)
    ExitButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
        (ScreenWidth // 2 - 110, ScreenHeight // 2 + 240), (220, 50)),
        text='Exit', manager=manager)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == MainMenu:
                    pygame.quit()
                    start_mainmenu()
                elif event.ui_element == Restart:
                    pygame.quit()
                    start_map()
                elif event.ui_element == ExitButton:
                    sys.exit()
            manager.process_events(event)

        manager.update(clock.tick(60))

        manager.draw_ui(screen)

        pygame.display.update()


