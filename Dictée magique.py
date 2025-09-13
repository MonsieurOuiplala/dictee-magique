import pygame # Pour jouer les sons
import random
import time
pygame.mixer.init()
def jouer_son(fichier):
	pygame.mixer.music.load(fichier)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():pass # Attendre jusqu'à la fin de la lecture

jouer_son("divers/allumage"+str(random.randrange(1,4))+".ogg")
print("Bienvenue dans la Dictée magique ! Chargement...")

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
				réponseÉpelle=input().lower()
				if réponseÉpelle=="répèter":jouer_mot()
				elif réponseÉpelle!=mot:
					if essai==0: # On a le droit a un second essai, bien sûr !
						jouer_son("divers/c'est_inexact_essaie_encore_une_fois.ogg")
						time.sleep(0.2)
						jouer_mot()
						essai+=1
					else:
						jouer_son("divers/c'est_inexact_la_bonne_ortographe_de.ogg")
						jouer_mot()
						jouer_son("divers/est.ogg")
						print(mot)
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
