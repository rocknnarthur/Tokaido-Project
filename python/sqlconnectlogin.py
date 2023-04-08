from mysql.connector import connect
import PySimpleGUI as sg  

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
    sql = ("SELECT jou_pseudo " "FROM Joueur " "WHERE jou_login = %s " "AND jou_password = %s;")
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