import pygame # Pour jouer les sons
import random
import time
pygame.mixer.init()
def jouer_son(fichier):
	pygame.mixer.music.load(fichier)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():pass # Attendre jusqu'à la fin de la lecture

jouer_son("divers/allumage"+str(random.randrange(1,4))+".ogg")
print("Bienvenue dans la Dictée Magique ! Chargement...")

def épelle(épelleNiveau):
	épelleListe=eval("épelle"+épelleNiveau) # Charger la liste des mots
	jouer_son("divers/épelle.ogg")
	nombreMots=10
	for i in range(nombreMots): # Nombre de mots personnalisable
			mot=random.choice(épelleListe) # Choisir le mot dans la liste clonée
			motEmplacement="épelle-"+épelleNiveau+"/"+mot+".ogg" # Emplacement de l'enregistrement du mot
			jouer_son(motEmplacement)
			time.sleep(0.1)
			# En attendant le système de frappe avec enregistrements
			réponseÉpelle=input().lower()
			if réponseÉpelle==mot:jouer_son("divers/"+random.choice(["la_réponse_est_bonne","bonne_réponse","c'est_correct"])+".ogg") # Sur la vraie Dictée Magique, les messages sont dans un ordre qui se répète. À implémenter
			else:
				jouer_son("divers/c'est_inexact_essaie_encore_une_fois.ogg") # Incorrect, on laisse une seconde chance...
				time.sleep(0.1)
				réponseÉpelle=input().lower()
				if réponseÉpelle==mot:jouer_son("divers/"+random.choice(["la_réponse_est_bonne","bonne_réponse","c'est_correct"])+".ogg") # Sur la vraie Dictée Magique, les messages sont dans un ordre qui se répète. À implémenter
				else:
					jouer_son("divers/c'est_inexact_la_bonne_ortographe_de.ogg")
					time.sleep(0.3)
					jouer_son(motEmplacement)
					time.sleep(0.3)
					jouer_son("divers/est.ogg")
					time.sleep(0.5)
					print(mot)
					time.sleep(1)
					jouer_son(motEmplacement)
			if i!=nombreMots-1:jouer_son("divers/maintenant_épelle.ogg")

dictéeÉpelle=["A"]
épelleA=["animal","bille","bol","camarade","canal","caramel","carnaval","carton","chaleur","chose","farine","feu","fille","fleur","fromage","marche","neveu","noir","parent","partir","potiron","poulet","premier","sardine","seul","sucre","tartine","tasse","tigre","trou","vendredi","ventre","vitrine"]
print("Terminé !")
time.sleep(1)
while True:
	print("\n"*5)
	demandeModeDeJeu=input("1 - Épelle\nfin - Éteindre la Dictée Magique\n")
	if demandeModeDeJeu=="1":
			print("\n"*2)
			for i in dictéeÉpelle:print("\nÉpelle "+i[0])
			épelle(input(""))
	if demandeModeDeJeu=="fin":break
