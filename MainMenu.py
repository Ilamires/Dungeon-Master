import sys
import pygame
import pygame_gui
import sqlite3


def start_mainmenu():
    from DungeonMaster import start_map
    from battle import start_battle
    pygame.init()
    pygame.display.set_caption('Dungeon Master')
    size1 = ScreenWidth, ScreenHeight = 1225, 700
    screen = pygame.display.set_mode(size1)
    DrawingCell = pygame.image.load("image/background/podzemelie_full.jpg")
    DrawingCell = pygame.transform.scale(DrawingCell, (1225, 700))
    screen.blit(DrawingCell, (0, 0))

    def Create_text(size, textvalue):
        Font = pygame.font.SysFont('Liberation Serif', size)
        text = Font.render(textvalue, False, (255, 255, 255))
        return text

    text = Create_text(100, 'Dungeon Master')
    text_rect = pygame.Rect(ScreenWidth // 2 - 340, 60, 800, 200)
    screen.blit(text, text_rect)

    manager = pygame_gui.UIManager((ScreenWidth, ScreenHeight))
    StatisticsRoom = False
    LoginRoom = False
    LoginAccount = False
    ContinueCreate = False
    Login = ''
    ContinueGame = ''
    Enter = ''
    Register = ''
    LogOutAccount = ''
    LogInAccount = ''
    Back = ''
    f = open('lastAccount.txt', mode='r')
    LastAccount, n = f.read().split('\n')
    if n != '':
        LoginAccount = True
        Login = n
    f.close()

    f = open('Continue.txt', mode='r')
    Continue = bool(int(f.read()))
    f.close()
    if Continue:
        if LastAccount == Login and LastAccount != '':
            ContinueCreate = True
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
    if LoginAccount:
        text = Create_text(30, Login)
        text_rect = pygame.Rect(10, 10, 80, 40)
        screen.blit(text, text_rect)
        LogOutAccount = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
            (400, 10), (200, 40)),
            text='Log Out Account', manager=manager)
    else:
        LogInAccount = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
            (10, 10), (200, 40)),
            text='Log In Account', manager=manager)

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
                    if LoginAccount:
                        f = open("mob_progression.txt", mode="w")
                        f.write(str(3))
                        f.close()
                        f = open('Continue.txt', mode='w')
                        f.write('0')
                        f.close()
                        f = open('ContinueBattle.txt', mode='w')
                        f.write('0')
                        f.close()
                        f = open('Hero.txt', mode='w')
                        f.write('100 0')
                        f.close()
                        f = open('StatisticsPerGame.txt', mode='w')
                        f.write('0 0 0')
                        f.close()
                        f = open('ReceivedArtefacts.txt', mode='w')
                        f.write('')
                        f.close()
                        pygame.quit()
                        running = False
                        start_map()
                    else:
                        LoginRoom = True
                        StartGame.kill()
                        StatisticsButton.kill()
                        ExitButton.kill()
                        LogInAccount.kill()
                        if ContinueCreate:
                            ContinueGame.kill()
                            ContinueCreate = False
                        screen.fill((0, 0, 0))
                        DrawingCell = pygame.image.load("image/background/podzemelie_full.jpg")
                        DrawingCell = pygame.transform.scale(DrawingCell, (1225, 700))
                        screen.blit(DrawingCell, (0, 0))
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
                        Back = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                            (ScreenWidth - 210, 10), (200, 50)),
                            text='Back', manager=manager)
                elif event.ui_element == StatisticsButton:
                    if LoginAccount:
                        StatisticsRoom = True
                        screen.fill((0, 0, 0))
                        DrawingCell = pygame.image.load("image/background/podzemelie_full.jpg")
                        DrawingCell = pygame.transform.scale(DrawingCell, (1225, 700))
                        screen.blit(DrawingCell, (0, 0))
                        text = Create_text(50, 'Killed Enemies:')
                        text_rect = pygame.Rect(ScreenWidth // 2 - 500, 100,
                                                90, 50)
                        screen.blit(text, text_rect)
                        text = Create_text(50, 'Wins:')
                        text_rect = pygame.Rect(ScreenWidth // 2, 100,
                                                90, 50)
                        screen.blit(text, text_rect)
                        text = Create_text(50, 'Loses:')
                        text_rect = pygame.Rect(ScreenWidth // 2 + 300, 100,
                                                90, 50)
                        screen.blit(text, text_rect)
                        AccFile = sqlite3.connect('accounts.sqlite3')
                        AccFileInf = AccFile.cursor()
                        KilledEnemies, Wins, Loses = list(AccFileInf.execute("""SELECT KilledEnemies, Wins, Loses FROM accounts
                                                WHERE Login=?""", (Login,)))[0]
                        text = Create_text(50, str(KilledEnemies))
                        text_rect = pygame.Rect(ScreenWidth // 2 - 350, 150,
                                                90, 50)
                        screen.blit(text, text_rect)
                        text = Create_text(50, str(Wins))
                        text_rect = pygame.Rect(ScreenWidth // 2 + 50, 150,
                                                90, 50)
                        screen.blit(text, text_rect)
                        text = Create_text(50, str(Loses))
                        text_rect = pygame.Rect(ScreenWidth // 2 + 350, 150,
                                                90, 50)
                        screen.blit(text, text_rect)
                        StartGame.kill()
                        StatisticsButton.kill()
                        ExitButton.kill()
                        if LoginAccount:
                            LogOutAccount.kill()
                        else:
                            LogInAccount.kill()
                        if ContinueCreate:
                            ContinueGame.kill()
                            ContinueCreate = False
                        Back = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                            (ScreenWidth - 210, 10), (200, 50)),
                            text='Back', manager=manager)
                    else:
                        LoginRoom = True
                        StartGame.kill()
                        StatisticsButton.kill()
                        ExitButton.kill()
                        LogInAccount.kill()
                        if ContinueCreate:
                            ContinueGame.kill()
                            ContinueCreate = False
                        screen.fill((0, 0, 0))
                        DrawingCell = pygame.image.load("image/background/podzemelie_full.jpg")
                        DrawingCell = pygame.transform.scale(DrawingCell, (1225, 700))
                        screen.blit(DrawingCell, (0, 0))
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
                        Back = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                            (ScreenWidth - 210, 10), (200, 50)),
                            text='Back', manager=manager)
                elif event.ui_element == ExitButton:
                    sys.exit()
                elif event.ui_element == LogInAccount:
                    LoginRoom = True
                    StartGame.kill()
                    StatisticsButton.kill()
                    ExitButton.kill()
                    LogInAccount.kill()
                    if ContinueCreate:
                        ContinueGame.kill()
                        ContinueCreate = False
                    screen.fill((0, 0, 0))
                    DrawingCell = pygame.image.load("image/background/podzemelie_full.jpg")
                    DrawingCell = pygame.transform.scale(DrawingCell, (1225, 700))
                    screen.blit(DrawingCell, (0, 0))
                    text = Create_text(30, 'Login')
                    text_rect = pygame.Rect(ScreenWidth // 2 - 98, ScreenHeight // 2 + 45,
                                            100, 50)
                    screen.blit(text, text_rect)
                    text = Create_text(30, 'Password')
                    text_rect = pygame.Rect(ScreenWidth // 2 - 98, ScreenHeight // 2 + 125,
                                            100, 50)
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
                    Back = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                        (ScreenWidth - 210, 10), (200, 50)),
                        text='Back', manager=manager)
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
                                    f = open('lastAccount.txt', mode='w')
                                    f.write(LastAccount + '\n' + Login)
                                    f.close()
                                    AccFile.commit()
                                    AccFile.close()
                                    screen.fill((0, 0, 0))
                                    DrawingCell = pygame.image.load("image/background/podzemelie_full.jpg")
                                    DrawingCell = pygame.transform.scale(DrawingCell, (1225, 700))
                                    screen.blit(DrawingCell, (0, 0))
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
                                        f = open('lastAccount.txt', mode='r')
                                        LastAccount = f.read().split('\n')[0]
                                        f.close()
                                        if LastAccount == Login and LastAccount != '':
                                            ContinueCreate = True
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
                                    LoginRoom = False
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
                            f = open('lastAccount.txt', mode='w')
                            f.write(LastAccount + '\n' + Login)
                            f.close()
                            AccFileChanger.execute("""INSERT INTO 
                                    accounts(Login,Password,Wins,Loses,KilledEnemies)
                                VALUES (?,?,?,?,?)""", (n, u, 0, 0, 0))
                            AccFile.commit()
                            AccFile.close()
                            screen.fill((0, 0, 0))
                            DrawingCell = pygame.image.load("image/background/podzemelie_full.jpg")
                            DrawingCell = pygame.transform.scale(DrawingCell, (1225, 700))
                            screen.blit(DrawingCell, (0, 0))
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
                                f = open('lastAccount.txt', mode='r')
                                LastAccount = f.read().split('\n')[0]
                                f.close()
                                if LastAccount == Login and LastAccount != '':
                                    ContinueCreate = True
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
                            LoginRoom = False
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
                elif event.ui_element == Back:
                    screen.fill((0, 0, 0))
                    DrawingCell = pygame.image.load("image/background/podzemelie_full.jpg")
                    DrawingCell = pygame.transform.scale(DrawingCell, (1225, 700))
                    screen.blit(DrawingCell, (0, 0))
                    if LoginRoom:
                        LoginRoom = False
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
                            f = open('lastAccount.txt', mode='r')
                            LastAccount = f.read().split('\n')[0]
                            f.close()
                            if LastAccount == Login and LastAccount != '':
                                ContinueCreate = True
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
                    elif StatisticsRoom == True:
                        StatisticsRoom = False
                        text = Create_text(100, 'Dungeon Master')
                        text_rect = pygame.Rect(ScreenWidth // 2 - 340, 60, 800, 200)
                        screen.blit(text, text_rect)
                        text = Create_text(30, Login)
                        text_rect = pygame.Rect(10, 10, 80, 40)
                        screen.blit(text, text_rect)
                        manager = pygame_gui.UIManager((ScreenWidth, ScreenHeight))
                        if Continue:
                            f = open('lastAccount.txt', mode='r')
                            LastAccount = f.read().split('\n')[0]
                            f.close()
                            if LastAccount == Login and LastAccount != '':
                                ContinueCreate = True
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
                        if LoginAccount:
                            text = Create_text(30, Login)
                            text_rect = pygame.Rect(10, 10, 80, 40)
                            screen.blit(text, text_rect)
                            LogOutAccount = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                (400, 10), (200, 40)),
                                text='Log Out Account', manager=manager)
                        else:
                            LogInAccount = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                (10, 10), (200, 40)),
                                text='Log In Account', manager=manager)
                elif event.ui_element == LogOutAccount:
                    LoginAccount = False
                    LogOutAccount.kill()
                    Login = ''
                    if ContinueCreate:
                        ContinueGame.kill()
                        pygame.draw.rect(screen, (0, 0, 0),
                                         (ScreenWidth // 2 - 100, ScreenHeight // 2, 200, 50), 0)
                    pygame.draw.rect(screen, (0, 0, 0),
                                     (10, 10, 900, 40), 0)
                    DrawingCell = pygame.image.load("image/background/podzemelie_full.jpg")
                    DrawingCell = pygame.transform.scale(DrawingCell, (1225, 700))
                    screen.blit(DrawingCell, (0, 0))
                    text = Create_text(100, 'Dungeon Master')
                    text_rect = pygame.Rect(ScreenWidth // 2 - 340, 60, 800, 200)
                    screen.blit(text, text_rect)
                    LogInAccount = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                        (10, 10), (200, 40)),
                        text='Log In Account', manager=manager)

            manager.process_events(event)

        manager.update(clock.tick(60))

        manager.draw_ui(screen)

        pygame.display.update()
