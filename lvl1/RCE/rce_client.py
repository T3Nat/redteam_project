import socket
import os

# Variable pour se connecter 
host = '<host>'
port = <port>
BUFFER = 4096

# Déclaration des sockets en TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

# On déclare une fonction pour crée notre commande
def commande():
    commande = input()
    s.sendall(commande.encode("utf-8"))

# Fonction pour recevoir
def receive():
    while True:
        try:
            commande() # On appelle la fonction pour envoyer la commande
            output = s.recv(BUFFER).decode("utf-8") # l'output de la réponse est stocké dans une variable
            print(output) # on affiche cette output
        except:
            print("Mauvaise commande") # si la commande renvoie rien on break la boucle infinie
            s.close() # on ferme le socket
            break # break
receive() # On appelle la fonction receive
