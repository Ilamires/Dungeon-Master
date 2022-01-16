import sys
import pygame
import pygame_gui
import sqlite3


def start_mainmenu():
    from DungeonMaster import start_map
    from battle import start_battle
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
        size1 = ScreenWidth, ScreenHeight = 1225, 700
        screen = pygame.display.set_mode(size1)

    def Create_text(size, textvalue):
        Font = pygame.font.SysFont('Liberation Serif', size)
        text = Font.render(textvalue, False, (255, 255, 255))
        return text

    text = Create_text(100, 'Dungeon Master')
    text_rect = pygame.Rect(ScreenWidth // 2 - 340, 60, 800, 200)
    screen.blit(text, text_rect)

    manager = pygame_gui.UIManager((ScreenWidth, ScreenHeight))
    LoginRoom = False
    LoginAccount = False
    f = open('Continue.txt', mode='r')
    Continue = bool(int(f.read()))
    f.close()
    if Continue:
        ContinueGame = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
            (ScreenWidth // 2 - 100, ScreenHeight // 2), (200, 50)),
            text='Continue', manager=manager)
    else:
        ContinueGame = ''
    StartGame = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
        (ScreenWidth // 2 - 100, ScreenHeight // 2 + 80), (200, 50)),
        text='Start game', manager=manager)
    StatisticsButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
        (ScreenWidth // 2 - 100, ScreenHeight // 2 + 160), (200, 50)),
        text='Statistics', manager=manager)
    ExitButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
        (ScreenWidth // 2 - 100, ScreenHeight // 2 + 240), (200, 50)),
        text='Exit', manager=manager)
    LogInAccount = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
        (10, 10), (200, 40)),
        text='Log In Account', manager=manager)
    Enter = ''
    Register = ''
    LogOutAccount = ''

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == ContinueGame:
                    pygame.quit()
                    running = False
                    f = open('ContinueBattle.txt', mode='r')
                    ContinueBattle = bool(int(f.read()))
                    f.close()
                    if ContinueBattle:
                        start_battle(0)
                    else:
                        start_map()
                elif event.ui_element == StartGame:
                    f = open('Continue.txt', mode='w')
                    f.write('0')
                    f.close()
                    f = open('ContinueBattle.txt', mode='w')
                    f.write('0')
                    f.close()
                    f = open('Hero.txt', mode='w')
                    f.write('100 0')
                    f.close()
                    pygame.quit()
                    running = False
                    start_map()
                elif event.ui_element == StatisticsButton:
                    pass
                elif event.ui_element == ExitButton:
                    sys.exit()
                elif event.ui_element == LogInAccount:
                    LoginRoom = True
                    StartGame.kill()
                    StatisticsButton.kill()
                    ExitButton.kill()
                    LogInAccount.kill()
                    if Continue:
                        ContinueGame.kill()
                    screen.fill((0, 0, 0))
                    text = Create_text(30, 'Login')
                    text_rect = pygame.Rect(ScreenWidth // 2 - 98, ScreenHeight // 2 + 45,
                                            800, 200)
                    screen.blit(text, text_rect)
                    text = Create_text(30, 'Password')
                    text_rect = pygame.Rect(ScreenWidth // 2 - 98, ScreenHeight // 2 + 125,
                                            800, 280)
                    screen.blit(text, text_rect)
                    LoginText = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(
                        (ScreenWidth // 2 - 100, ScreenHeight // 2 + 80), (200, 50)),
                        manager=manager)
                    PasswordText = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(
                        (ScreenWidth // 2 - 100, ScreenHeight // 2 + 160), (200, 50)),
                        manager=manager)
                    Enter = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                        (ScreenWidth // 2 - 100, ScreenHeight // 2 + 200), (200, 50)),
                        text='Enter', manager=manager)
                    Register = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                        (ScreenWidth // 2 - 100, ScreenHeight // 2 + 240), (200, 50)),
                        text='Register', manager=manager)
                elif event.ui_element == Enter:
                    pygame.draw.rect(screen, (0, 0, 0),
                                     (ScreenWidth // 2 - 98, ScreenHeight // 2 + 300, 240, 80), 0)
                    n = LoginText.text
                    p = PasswordText.text
                    s = ''
                    m = True
                    AccFile = sqlite3.connect('accounts.sqlite3')
                    AccFileInf = AccFile.cursor()
                    AccInf = AccFileInf.execute("""SELECT Login,Password FROM accounts""").fetchall()
                    u = ''
                    for j in p:
                        u += str(ord(j)) + ' '
                    try:
                        for i in AccInf:
                            if n == i[0]:
                                if u == i[1]:
                                    LoginAccount = True
                                    Login = n
                                    AccFile.commit()
                                    AccFile.close()
                                    screen.fill((0, 0, 0))
                                    LoginText.kill()
                                    PasswordText.kill()
                                    Enter.kill()
                                    Register.kill()
                                    text = Create_text(100, 'Dungeon Master')
                                    text_rect = pygame.Rect(ScreenWidth // 2 - 340, 60, 800, 200)
                                    screen.blit(text, text_rect)
                                    text = Create_text(30, Login)
                                    text_rect = pygame.Rect(10, 10, 80, 40)
                                    screen.blit(text, text_rect)
                                    manager = pygame_gui.UIManager((ScreenWidth, ScreenHeight))
                                    if Continue:
                                        ContinueGame = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                            (ScreenWidth // 2 - 100, ScreenHeight // 2), (200, 50)),
                                            text='Continue', manager=manager)
                                    StartGame = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                        (ScreenWidth // 2 - 100, ScreenHeight // 2 + 80), (200, 50)),
                                        text='Start game', manager=manager)
                                    StatisticsButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                        (ScreenWidth // 2 - 100, ScreenHeight // 2 + 160), (200, 50)),
                                        text='Statistics', manager=manager)
                                    ExitButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                        (ScreenWidth // 2 - 100, ScreenHeight // 2 + 240), (200, 50)),
                                        text='Exit', manager=manager)
                                    LogOutAccount = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                        (400, 10), (200, 40)),
                                        text='Log Out Account', manager=manager)
                                    m = False
                                    break
                                else:
                                    s = 'Invalid password.'
                                    raise ValueError(s)
                        if m:
                            s = 'This user does not exist.'
                            raise NameError(s)
                    except NameError:
                        text = Create_text(20, s)
                        text_rect = pygame.Rect(ScreenWidth // 2 - 98, ScreenHeight // 2 + 300,
                                                80, 20)
                        screen.blit(text, text_rect)
                    except ValueError:
                        text = Create_text(20, s)
                        text_rect = pygame.Rect(ScreenWidth // 2 - 98, ScreenHeight // 2 + 300,
                                                80, 20)
                        screen.blit(text, text_rect)
                elif event.ui_element == Register:
                    pygame.draw.rect(screen, (0, 0, 0),
                                     (ScreenWidth // 2 - 98, ScreenHeight // 2 + 300, 240, 80), 0)
                    n = LoginText.text
                    p = PasswordText.text
                    s = ''
                    AccFile = sqlite3.connect('accounts.sqlite3')
                    AccFileChanger = AccFile.cursor()
                    AccFileInf = AccFile.cursor()
                    AccInf = AccFileInf.execute("""SELECT Login FROM accounts""").fetchall()
                    u = ''
                    for j in p:
                        u += str(ord(j)) + ' '
                    try:
                        NicknameTaken = False
                        for i in AccInf:
                            if n == i[0]:
                                NicknameTaken = True
                                break
                        if len(n) > 20:
                            s = 'The nickname is too long.'
                            raise NameError(s)
                        elif NicknameTaken:
                            s = 'This name is already taken.'
                            raise NameError(s)
                        elif len(p) < 8:
                            s = 'The password is too short.'
                            raise ValueError(s)
                        elif len(p) > 20:
                            s = 'The password is too long.'
                            raise ValueError(s)
                        else:
                            LoginAccount = True
                            Login = n
                            AccFileChanger.execute("""INSERT INTO 
                                    accounts(Login,Password,Wins,Loses,KilledEnemies)
                                VALUES (?,?,?,?,?)""", (n, u, 0, 0, 0))
                            AccFile.commit()
                            AccFile.close()
                            screen.fill((0, 0, 0))
                            LoginText.kill()
                            PasswordText.kill()
                            Enter.kill()
                            Register.kill()
                            text = Create_text(100, 'Dungeon Master')
                            text_rect = pygame.Rect(ScreenWidth // 2 - 340, 60, 800, 200)
                            screen.blit(text, text_rect)
                            text = Create_text(30, Login)
                            text_rect = pygame.Rect(10, 10, 80, 40)
                            screen.blit(text, text_rect)
                            manager = pygame_gui.UIManager((ScreenWidth, ScreenHeight))
                            if Continue:
                                ContinueGame = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                    (ScreenWidth // 2 - 100, ScreenHeight // 2), (200, 50)),
                                    text='Continue', manager=manager)
                            StartGame = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                (ScreenWidth // 2 - 100, ScreenHeight // 2 + 80), (200, 50)),
                                text='Start game', manager=manager)
                            StatisticsButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                (ScreenWidth // 2 - 100, ScreenHeight // 2 + 160), (200, 50)),
                                text='Statistics', manager=manager)
                            ExitButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                (ScreenWidth // 2 - 100, ScreenHeight // 2 + 240), (200, 50)),
                                text='Exit', manager=manager)
                            LogOutAccount = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                (400, 10), (200, 40)),
                                text='Log Out Account', manager=manager)
                    except NameError:
                        text = Create_text(20, s)
                        text_rect = pygame.Rect(ScreenWidth // 2 - 98, ScreenHeight // 2 + 300,
                                                80, 20)
                        screen.blit(text, text_rect)
                    except ValueError:
                        text = Create_text(20, s)
                        text_rect = pygame.Rect(ScreenWidth // 2 - 98, ScreenHeight // 2 + 300,
                                                80, 20)
                        screen.blit(text, text_rect)
                elif event.ui_element == LogOutAccount:
                    LoginAccount = False
                    LogOutAccount.kill()
                    pygame.draw.rect(screen, (0, 0, 0),
                                     (10, 10, 900, 40), 0)
                    LogInAccount = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                        (10, 10), (200, 40)),
                        text='Log In Account', manager=manager)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and not LoginRoom:
                    DisplaySize = pygame.display.get_window_size()
                    pygame.quit()
                    pygame.init()
                    pygame.display.set_caption('Dungeon Master')
                    if DisplaySize == (1225, 700):
                        size = ScreenWidth, ScreenHeight = pygame.display.Info().current_w, \
                                                           pygame.display.Info().current_h
                        screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
                        f = open('Fullscreen.txt', mode='w')
                        f.write('1')
                        f.close()
                    else:
                        size = ScreenWidth, ScreenHeight = 1225, 700
                        screen = pygame.display.set_mode(size)
                        f = open('Fullscreen.txt', mode='w')
                        f.write('0')
                        f.close()
                    if LoginRoom:
                        LoginText.kill()
                        PasswordText.kill()
                        text = Create_text(30, 'Login')
                        text_rect = pygame.Rect(ScreenWidth // 2 - 98, ScreenHeight // 2 + 45,
                                                800, 200)
                        screen.blit(text, text_rect)
                        text = Create_text(30, 'Password')
                        text_rect = pygame.Rect(ScreenWidth // 2 - 98, ScreenHeight // 2 + 125,
                                                800, 280)
                        screen.blit(text, text_rect)

                        manager = pygame_gui.UIManager((ScreenWidth, ScreenHeight))
                        LoginText = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(
                            (ScreenWidth // 2 - 100, ScreenHeight // 2 + 80), (200, 50)),
                            manager=manager)
                        PasswordText = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(
                            (ScreenWidth // 2 - 100, ScreenHeight // 2 + 160), (200, 50)),
                            manager=manager)
                    else:
                        text = Create_text(100, 'Dungeon Master')
                        text_rect = pygame.Rect(ScreenWidth // 2 - 340, 60, 800, 200)
                        screen.blit(text, text_rect)
                        StartGame.kill()
                        StatisticsButton.kill()
                        ExitButton.kill()
                        LogInAccount.kill()
                        if Continue:
                            ContinueGame.kill()
                        manager = pygame_gui.UIManager((ScreenWidth, ScreenHeight))
                        if Continue:
                            ContinueGame = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                (ScreenWidth // 2 - 100, ScreenHeight // 2), (200, 50)),
                                text='Continue', manager=manager)
                        StartGame = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                            (ScreenWidth // 2 - 100, ScreenHeight // 2 + 80), (200, 50)),
                            text='Start game', manager=manager)
                        StatisticsButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                            (ScreenWidth // 2 - 100, ScreenHeight // 2 + 160), (200, 50)),
                            text='Statistics', manager=manager)
                        ExitButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                            (ScreenWidth // 2 - 100, ScreenHeight // 2 + 240), (200, 50)),
                            text='Exit', manager=manager)
                        LogInAccount = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                            (10, 10), (200, 40)),
                            text='Log In Account', manager=manager)

            manager.process_events(event)

        manager.update(clock.tick(60))

        manager.draw_ui(screen)

        pygame.display.update()
