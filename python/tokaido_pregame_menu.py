import pygame
import pygame_menu
from classes import Crosshair

pygame.init()
pygame.display.set_caption("Game settings")
pygame.display.set_icon(pygame.image.load("python/images/sakura.png"))
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((1280, 720))

# crosshair
crosshair = Crosshair("python/images/sakura_flower.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)


# FUNCTIONS GET VALUES
def set_difficulty(selected, value) -> None:
    global mode

    """
    Set the difficulty of the game.
    """
    print(f'Set difficulty to {selected[0][0]} ({value})')
    mode = value

def set_player_nbr(selected, value) -> None:
    global n_player

    """
    Set the number of players in the game.
    """
    print(f'Set player number to {selected[0][0]} ({value})')
    n_player = value

def set_color(selected, value) -> None:
    global color

    """
    Set the color of players in the game.
    """
    print(f'Set player number to {selected[0][0]} ({value})')
    color = selected[0]

# LOOP MENUS
def main_menu():

    global mode

    mode = 0

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        # Draw the menu
        surface.fill((25, 0, 50))

        menu.update(events)
        menu.draw(surface)

        crosshair_group.draw(surface)
        crosshair_group.update()
        pygame.display.flip()

def menu_nbr_player():
    global n_player
    n_player = 2

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        # Draw the menu
        surface.fill((25, 0, 50))

        menu2.update(events)
        menu2.draw(surface)

        crosshair_group.draw(surface)
        crosshair_group.update()
        pygame.display.flip()

def menu_color():

    global color

    l_color = [('purple', 1), ('yellow', 2), ('green', 3), ('gray', 4), ('blue', 5)]
    for n in range(1, n_player+1):
        color = l_color[0]

        menu3.add.selector(f'Couleur joueur {n}: ', l_color, onchange=set_color)
        menu3.add.button('Next', None)
        menu3.add.button('Quit', pygame_menu.events.EXIT)

        menu3.select_widget(None)

        while True:

            next = menu3.get_selected_widget().get_title()
            if next == 'Next':
                print("ok")
                break

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

            # Draw the menu
            surface.fill((25, 0, 50))

            menu3.update(events)
            menu3.draw(surface)

            crosshair_group.draw(surface)
            crosshair_group.update()
            pygame.display.flip()

        print(color)
        l_color.remove(color)
        menu3.close()


#def start_the_game() -> None:
    #"""
    #Function that starts a game. This is raised by the menu button,
    #here menu can be disabled, etc.
    #"""
    #global user_name
    #print(f'{user_name.get_value()}, Do the job here!')


menu = pygame_menu.Menu(
    width=1280,
    height=720,
    theme=pygame_menu.themes.THEME_DARK,
    title='Gamemode'
)

menu2 = pygame_menu.Menu(
    width=1280,
    height=720,
    theme=pygame_menu.themes.THEME_DARK,
    title='Nombre de joueurs'
)

menu3 = pygame_menu.Menu(
    width=1280,
    height=720,
    theme=pygame_menu.themes.THEME_DARK,
    title='Choix des couleurs'
)

#user_name = menu.add.text_input('Name: ', default='John Doe', maxchar=10)
menu.add.selector('Mode: ', [('Noob Travel', 0), ('Normal Travel', 1), ('Back Travel', 2), ('Gastronomy Travel', 3), ('Setups Travel', 4)], onchange=set_difficulty)
menu.add.button('Next', menu_nbr_player)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu2.add.selector('Nombre joueurs: ', [('2', 2), ('3', 3), ('4', 4), ('5', 5)], onchange=set_player_nbr)
menu2.add.button('Next', menu_color)
menu2.add.button('Quit', pygame_menu.events.EXIT)


main_menu()
    
