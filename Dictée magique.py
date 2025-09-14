import pygame # Pour jouer les sons
import random
import time
import sys, tty, termios # Pour le clavier
pygame.mixer.init()
def jouer_son(fichier):
	pygame.mixer.music.load(fichier)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():pass # Attendre jusqu'à la fin de la lecture
def jouer_lettre(lettre):jouer_son("alphabet/"+lettre+".ogg") # Joue par exemple alphabet/a.ogg
def épelle_input():
	fd=sys.stdin.fileno()
	ancien=termios.tcgetattr(fd)
	try:
		tty.setraw(fd)
		touche=sys.stdin.read(1)  # Lit une seule touche
	finally:termios.tcsetattr(fd,termios.TCSADRAIN,ancien)
	return touche

def épeller_mot(épellerMot,afficher=True):
	épellerMot=list(épellerMot)
	for lettre in épellerMot:
		if afficher:print(lettre,end="",flush=True)
		jouer_lettre(lettre)
		time.sleep(0.06)

jouer_son("divers/allumage"+str(random.randrange(1,4))+".ogg")
print("Bienvenue dans la Dictée magique ! Chargement...")

def épelle_clavier(épelleNiveau,motÉpelle):
	mot=""
	print()
	while True:
		caractère=épelle_input()
		if caractère=='"':jouer_son("épelle-"+épelleNiveau+"/"+motÉpelle+".ogg") # Touche pour répéter le mot
		elif caractère=="'":
			print("") # Touche pour recommencer
			mot=""
		elif caractère in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
			mot+=caractère
			jouer_lettre(caractère)
			print(caractère,end="",flush=True)
		elif caractère==" ": # caractère ne porte pas très bien son nom...
			return mot
			break
	

def épelle(épelleNiveau):
	épelleListe=eval("épelle"+épelleNiveau) # Charger la liste des mots
	jouer_son("divers/épelle.ogg")
	bonneRéponseRéponses=["bonne_réponse_maintenant_épelle","c'est_correct_épelle_ensuite","la_réponse_est_bonne_épelle","c'est_correct"]	
	bonneRéponses=[0,1,2,1,0,1,2,1,0,3] # Dans l'ordre de lecture des bonnes réponses, bonneRéponseRéponses[i]
	def bonneRéponse():
		jouer_son("divers/"+bonneRéponseRéponses[bonneRéponses[0]]+".ogg")
		del bonneRéponses[0]
	nombreMots=10
	for i in range(nombreMots): # Nombre de mots personnalisable
			mot=random.choice(épelleListe) # Choisir le mot dans la liste clonée
			def jouer_mot():jouer_son("épelle-"+épelleNiveau+"/"+mot+".ogg") # Emplacement de l'enregistrement du mot
			jouer_mot()
			time.sleep(0.1)
			essai=0
			while True:
				réponseÉpelle=épelle_clavier(épelleNiveau,mot)
				if réponseÉpelle!=mot:
					if essai==0: # On a le droit a un second essai, bien sûr !
						jouer_son("divers/c'est_inexact_essaie_encore_une_fois.ogg")
						time.sleep(0.2)
						jouer_mot()
						essai+=1
					else:
						jouer_son("divers/c'est_inexact_la_bonne_ortographe_de.ogg")
						jouer_mot()
						jouer_son("divers/est.ogg")
						print("")
						épeller_mot(mot)
						time.sleep(1)
						jouer_mot()
						time.sleep(0.1)
						jouer_son("divers/épelle.ogg")
						break
				else:
					bonneRéponse()
					break
			del épelleListe[épelleListe.index(mot)] # On supprime le mot du clone de la liste de mots, pour ne pas retomber dessus
	jouer_son("divers/fin.ogg")

dictéeÉpelle=["A","B"]
épelleA=["animal","bille","bol","camarade","canal","caramel","carnaval","carton","chaleur","chose","farine","feu","fille","fleur","fromage","marche","neveu","noir","parent","partir","potiron","poulet","premier","sardine","seul","sucre","tartine","tasse","tigre","trou","vendredi","ventre","vitrine"]
épelleB=["acier","besoin","blouse","bois","campeur","chaise","chance","chanson","chienne","cousin","deux","dindon","espoir","fleuve","froid","gant","jambon","lange","ligne","long","montagne","orange","pantalon","poison","poisson","quille","raisin","renard","six","soigner","valise","voyage"]
print("Terminé !")
time.sleep(1)
while True:
	print("\n"*4)
	demandeModeDeJeu=input("1 - Épelle\nfin - Éteindre la Dictée magique\n")
	if demandeModeDeJeu=="1":
			print("\n"*4)
			for i in dictéeÉpelle:print("Épelle "+i[0])
			épelle(input(""))
	if demandeModeDeJeu=="fin":break
