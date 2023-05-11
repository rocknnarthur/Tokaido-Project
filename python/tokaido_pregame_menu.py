import pygame
import pygame_menu

pygame.init()
pygame.display.set_caption("Game settings")
surface = pygame.display.set_mode((1280, 720))

# FUNCTIONS GET VALUES
def set_difficulty(selected, value) -> None:
    global difficulty

    """
    Set the difficulty of the game.
    """
    print(f'Set difficulty to {selected[0][0]} ({value})')
    difficulty = value

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
    Set the number of players in the game.
    """
    print(f'Set player number to {selected[0][0]} ({value})')
    color = selected[0][0]

# LOOP MENUS
def menu_nbr_player():
    menu2.mainloop(surface)

def menu_color():
    menu3.mainloop(surface)


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

menu3.add.selector('Couleur: ', [('purple', 1), ('yellow', 2), ('green', 3), ('gray', 4), ('blue', 5)], onchange=set_player_nbr)
menu3.add.button('Next', None)
menu3.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)