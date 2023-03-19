import mysql.connector
from datetime import date, datetime

cnx = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root",
  database="tokaido"
)
print(cnx)
cursor = cnx.cursor()

today = datetime.now().date()

add_joueur = ("INSERT INTO Joueur "
               "(jou_id, jou_nom, jou_prenom, jou_pseudo, jou_creation, jou_login, jou_password) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")

data_joueur = (2, "AMISI", "Arthur", "Vitarse", today, "vitarse", "azerty123*")

row = """\nINSERT INTO Joueur (jou_id, jou_nom, jou_prenom, jou_pseudo, jou_creation, jou_login, jou_password)
VALUES (2, "AMISI", "Arthur", "Vitarse", today, "vitarse", "azerty123*");"""

fic = open("../sql/tokaido.sql", "a")
fic.write(row)
fic.close

# Insert new employee
cursor.execute(add_joueur, data_joueur)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()