import socket
import threading

# On définit le socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'host'
port = 11223
# On choisit un pseudo
pseudo = input("Choississez votre pseudo")

BUFFER = 1024 # On définit notre buffer à 1024 octets

# On se connecte au serveur avec une fonction useless
def connexion_server():
    s.connect((host,port))

connexion_server() # HAHA C'EST DRÔLE

def receive(): # On définit la fonction recevoir pour recevoir les données du serveur
    while True:
        try:
            # On reçoit le message du serveur
            # Si on reçoit 'PSEUDO' on envoit notre pseudo qu'on decode en ascii
            message = s.recv(BUFFER).decode("utf-8")
            if message == 'PSEUDO':
                s.send(pseudo.encode("utf-8"))
            else:
                print(message)
        except:
            # On ferme la connexion quand on a une erreur dans le try catch
            print("Erreur de connexion")
            s.close() # on ferme le socket
            break

def write(): # On définit une fonction pour envoyer un message à travers le socket
    while True: # Boucle infinit
        message = (f'{pseudo} {input()}') # Dans le message on stock deux variables, notre pseudo et notre message à travers la fonction intégré input
        s.send(message.encode("utf-8")) # on envoie le message encode en ascii vu que le serveur le decode tout le temps en ascii
        

# On définit dans cette fonction deux threads qui vont target les fonctions receive et write et ensuite on l'appelle pour lancer ces deux fonctions en deux process simultanés
recv_thread = threading.Thread(target=receive)
recv_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()
