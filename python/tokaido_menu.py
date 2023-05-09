import pygame, sys
from button import Button
from sqlconnectlogin import get_stat
from fichier import Fichier

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Tokaido Menu")
pygame.display.set_icon(pygame.image.load("python/images/sakura.png"))

menu_bg = pygame.image.load("python/images/menu.jpg")
options_bg = pygame.image.load("python/images/settings.jpg")
account_bg = pygame.image.load("python/images/account.jpg")

def get_font(size): # Returns the BTTTRIAL font in the specify size
    return pygame.font.Font("python/BTTTRIAL.otf", size)
def get_font2(size): # Returns the Calibri font in the specify size
    return pygame.font.Font("python/calibri.ttf", size)

def play():
    pygame.display.set_caption("Tokaido")

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Gray")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    pygame.display.set_caption("Options")

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(options_bg, (-320, -70))

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Gray")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def account():
    pygame.display.set_caption("Compte Tokaido")
    get_stat()
    r = Fichier("connected_account.dat").lire()
    r2 = Fichier("connected_account_stat.dat").lire()

    while True:
        ACCOUNT_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(account_bg, (-320, -70))

        ACCOUNT_TEXT = get_font2(45).render(f"Statistiques de {r[0][3]}", True, "Gray")
        ACCOUNT_TEXT2 = get_font2(45).render(f"Victoire : {r2[0][0]}", True, "Green")
        ACCOUNT_TEXT3 = get_font2(45).render(f"Défaite : {r2[0][1]}", True, "Red")
        ACCOUNT_RECT = ACCOUNT_TEXT.get_rect(center=(640, 260))
        ACCOUNT_RECT2 = ACCOUNT_TEXT2.get_rect(center=(640, 310))
        ACCOUNT_RECT3 = ACCOUNT_TEXT3.get_rect(center=(640, 360))
        SCREEN.blit(ACCOUNT_TEXT, ACCOUNT_RECT)
        SCREEN.blit(ACCOUNT_TEXT2, ACCOUNT_RECT2)
        SCREEN.blit(ACCOUNT_TEXT3, ACCOUNT_RECT3)

        ACCOUNT_BACK = Button(image=None, pos=(640, 560), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Gray")

        ACCOUNT_BACK.changeColor(ACCOUNT_MOUSE_POS)
        ACCOUNT_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ACCOUNT_BACK.checkForInput(ACCOUNT_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    pygame.display.set_caption("Tokaido Menu")

    while True:
        SCREEN.blit(menu_bg, (-320, -70))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("TOKAIDO", True, "#9BCCA4")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 190))

        PLAY_BUTTON = Button(image=None, pos=(640, 325), 
                            text_input="PLAY", font=get_font(70), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=None, pos=(640, 435), 
                            text_input="OPTIONS", font=get_font(70), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(640, 545), 
                            text_input="QUIT", font=get_font(70), base_color="#d7fcd4", hovering_color="White")
        ACCOUNT_BUTTON = Button(image=None, pos=(150, 60),
                            text_input="COMPTE", font=get_font(50), base_color="#000000", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, ACCOUNT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if ACCOUNT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    account()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()