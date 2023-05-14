import pickle

fichier_positions = open("positions_data.txt","rb")
position_list = pickle.load(fichier_positions)
fichier_positions.close()

fichier_positions = open("positions_data2.txt","rb")
position_list2 = pickle.load(fichier_positions)
fichier_positions.close()

fichier_positions = open("positions_dataInter.txt","rb")
position_listInter = pickle.load(fichier_positions)
fichier_positions.close()

print(f"position stop 1: {position_list}")
print(f"position stop 2: {position_list2}")
print(f"position stop 3: {position_listInter}")