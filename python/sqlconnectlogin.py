from mysql.connector import connect
import PySimpleGUI as sg
from fichier import Fichier

# Variable globale result que l'on retrouve dans la fonction connexion
result = None
def connexion(idt, mdp):

    global result

    cnx = connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="tokaido"
        )
    
    print(cnx)
    cursor = cnx.cursor()

    # requête qui AFFICHE tout identifiant
    sql = ("SELECT * " "FROM Joueur " "WHERE jou_login = %s " "AND jou_password = %s;")
    data = (f"{idt}", f"{mdp}")

    # on exécute la requête
    cursor.execute(sql, data)
    result = cursor.fetchall()
    print(result)

    cnx.commit()
    cursor.close()
    cnx.close()

    if len(result) >= 1:
        print("TROUVE")
        return True
    else: 
        print("PAS TROUVE")
        return False


def get_stat():

    cnx = connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="tokaido"
        )
    
    print(cnx)
    cursor = cnx.cursor()

    r = Fichier("connected_account.dat").lire()

    # requête qui AFFICHE tout identifiant
    sql = ("SELECT sta_win, sta_lose " "FROM Joueur " "INNER JOIN Statistiques " "ON jou_id = sta_id " "WHERE jou_login = %s " "AND jou_password = %s;")
    data = (f"{r[0][5]}", f"{r[0][6]}")

    # on exécute la requête
    cursor.execute(sql, data)
    result2 = cursor.fetchall()
    Fichier("connected_account_stat.dat").ecrire(result2)
    print(result2)

    cnx.commit()
    cursor.close()
    cnx.close()