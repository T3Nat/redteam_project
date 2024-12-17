import threading
import socket

host = ''
port = 11223
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
BUFFER = 1024


# Petit délire de création de fonction useless parce que j'ai envie

def start_server(): # Fonction pour bind et mettre en écoute le serveur
    s.bind((host,port))
    s.listen()

def close_server(): # Fonction pour fermer le serveur
    s.close()


    client, addr = s.accept()

start_server() # On start le serveur avec notre fonction useless

# On crée des listes vides pour stocket le pseudo des clients et leurs nombres

clients = []
pseudo = []

def broad(message): # On définit une fonction pour faire un broadcast d'un message qui sera diffuser aux yeux de tous les clients
    for client in clients: # Pour chaque client dans la liste "clients" on envoie le message de broadcast
        client.send(message)
        
def handle(client): # Cette fonction permet de prendre en charge les connexionx, elle se break une fois les clients partis du socket
    while True:
        try:
            # On broadcast le message
            message = client.recv(BUFFER) # Le buffer est de 1024 octets de bases
            broad(message)
        except:
            # On enlève et on ferme les clients
            index = clients.index(client) # On crée un index qui va pointer sur chaque clients dans la liste "clients"
            clients.remove(client) # Suite à ce pointage on remove les différents clients de la liste "clients"
            clients.close() # On coupe la connexion socket avec les clients
            pseudo = pseudo[index] # On crée un index pour pointer dans la liste "pseudo" appartenant aux clients
            broad((f'{pseudo} left like a coward nigga').encode('utf-8')) # Pour chaque clients don la connexion est fermé on renvoit son pseudo dans le terminal avec un message " left !"
            pseudo.remove(pseudo) # on pointe sur les pseudo qu'on remove de la liste
            break # on break la loop

def receive():
    while True : # Boucle infinie, indispensable quand on traite des connexions entrante
        client, addr = s.accept() # On appelle l'acceptation de connexion
        print((f"Connecté avec {addr}").encode("utf-8")) # On retourne les adresses des connexions entrantes qui sont celles avec qui on discute
        
        
        # Stockage des pseudo
        client.send(('PSEUDO').encode("utf-8"))
        pseudos = client.recv(BUFFER).decode("utf-8") # On définit le pseudo ( on le reçoit en premier )
        pseudos = pseudo.append(pseudos) # On ajout 'PSEUDO' au pseudo que l'on reçoit
        clients.append(client) # On concatene le nom du client aux pseudo
        
        # On affiche les pseudo et on les envoie en broadcast pour que tous le monde les vois
        print(f"Le pseudo est {pseudo}") # On affiche le pseudo
        broad((f"{pseudo} a rejoint !").encode("utf-8")) # On notifie que intel à rejoint le serveur
        notif_connexion = 'Connecte au serveur'.encode("utf-8") # variable contenant la notification que intel a rejoint
        client.send(notif_connexion) # on envoie au client le retour de la notification
        
        # On définit un threading avec la fonction 'handle' pour un meilleur traitment
        thread = threading.Thread(target=handle, args=(client,)) # On définit un argument client ('fonctionne comme les sockets')
        thread.start() # on start le thread 

receive() # On appel la fonction receive 
