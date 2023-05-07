import PySimpleGUI as sg
import sqlconnectlogin
from sqlconnectlogin import connexion

layout = [
        [sg.Text("Bienvenue voyageur !", key="head", font=('Pristina', (30)))],
        [sg.Text("Identifiant:", font=('Pristina', (20)))],
        [sg.Input(key="id")],
        [sg.Text("Mot de passe:", font=('Pristina', (20)))],
        [sg.Input(key="mdp")],
        [sg.Text(key="error", text_color="darkred", font=('Pristina', (15)))],
        [sg.Button("Log In", size=(8,0), font=('Pristina', (15))), sg.Button("Sign Up", size=(8,0), font=('Pristina', (15))), sg.Exit("Quit", size=(8,0), font=('Pristina', (15)))]
        ]
window = sg.Window("CONNEXION TOKAIDO", layout, icon = 'python/images/tokaido-connexion.ico', size=(720,360), default_element_size=(200, 200))

while True:
    event , values = window.read()

    if event == sg.WIN_CLOSED or event == "Quit":
        break

    # Check login entrance
    if event == "Log In":

        idt = str(values['id'])
        mdp = str(values['mdp'])

        if connexion(idt, mdp):
            print(f"Bienvenue à vous {sqlconnectlogin.result[0][0]} !")
            window['error'].Update("")
            window.close()
        
        else:
            window['id'].Update("")
            window['mdp'].Update("")
            window['error'].Update("Identifiant ou mot de passe incorrect, veuillez réessayer.")


    if event == "Sign Up":
        sg.Popup("Création de compte")

window.close()