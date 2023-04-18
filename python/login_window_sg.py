import PySimpleGUI as sg
import sqlconnectlogin
from sqlconnectlogin import connexion

layout = [
        [sg.Text("Bienvenue voyageur !", key="head", auto_size_text=True)],
        [sg.Text("Identifiant:")],
        [sg.Input(key="id")],
        [sg.Text("Mot de passe:")],
        [sg.Input(key="mdp")],
        [sg.Text(key="error", text_color="darkred")],
        [sg.Button("Log In"), sg.Button("Sign Up"), sg.Exit("Quit")]
        ]
window = sg.Window("CONNEXION TOKAIDO", layout, icon = r'python/images/tokaido-connexion.ico', size=(1080,720))

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