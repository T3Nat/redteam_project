import os
import socket
import tqdm

BUFFER=1024   # On définit le buffer
 
host = ''  # Host et port que l'on va bond pour écouter
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Définition du socket, en tcp
s.bind((host,port)) # On définit sur quel adresse et port on bind le socket
s.listen() # On met le socket en écoute
conn, addr = s.accept() # On différencie l'acceptation de connexion entre celle qui vient de notre adresse à celle qui vient de l'extérieur

file_name = conn.recv(BUFFER).decode() # Dans la première partie de la connexion se trouve le nom du fichier
print(f"{file_name}\n") # On l'affiche pour s'apercevoir de l'erreur si jamais l'output 
file_size = conn.recv(BUFFER).decode() # En deuxième temps on reçoit la taille du fichier qui va servir dans la progression du transfert
print(f"{file_size}\n")

file = open(file_name, "wb") # On ouvre en write bytes le fichier don on reçoit le nom
file_bytes = b'' # On définit les bytes en vide pour l'instant
done = False # Un booléen

progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size)) # Création d'une progression

while not done: # while True en gros 
    data = conn.recv(BUFFER) # On stock le contenu du fichier dans un variable "data"
    if file_bytes[-5:] == b"<END>": #Vérifie les 5 derniers octets de la variables file_byte et si la valeurs <END> s'y trouve
        done = True   # done passe en true et on sort de la boucle
    else:
        file_bytes += data # on concatène file_byte et la data
    progress.update(BUFFER) # on fait passer les bytes dans la progress bar

file.write(file_bytes) # on écrit les données dans le fichier
conn.close()
s.close()
