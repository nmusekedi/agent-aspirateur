import pygame
import time
from config import *

class AgentAspirateur:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (60, 60))

        self.x = CHAMBRE_A_POS[0] + 60
        self.y = 50

        self.nettoyages = 0
        self.logs = []
        self.derniere_chambre = None

    def log(self, message):
        timestamp = time.strftime("%H:%M:%S")
        self.logs.append(f"[{timestamp}] {message}")
        self.logs = self.logs[-6:]  # garder derniers logs

        with open("logs/actions.log", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")

    def deplacer_vers(self, position):
        self.x = position[0] + 60

    def agir(self, chambre_a, chambre_b):

        # Cas 1 : les deux chambres sont sales
        if chambre_a.sale and chambre_b.sale:
            if self.derniere_chambre == "A":
                self.deplacer_vers(CHAMBRE_B_POS)
                chambre_b.nettoyer()
                self.derniere_chambre = "B"
                self.nettoyages += 1
                self.log("Nettoyage chambre B")
            else:
                self.deplacer_vers(CHAMBRE_A_POS)
                chambre_a.nettoyer()
                self.derniere_chambre = "A"
                self.nettoyages += 1
                self.log("Nettoyage chambre A")

        # Cas 2 : seule la chambre A est sale
        elif chambre_a.sale:
            self.deplacer_vers(CHAMBRE_A_POS)
            chambre_a.nettoyer()
            self.derniere_chambre = "A"
            self.nettoyages += 1
            self.log("Nettoyage chambre A")

        # Cas 3 : seule la chambre B est sale
        elif chambre_b.sale:
            self.deplacer_vers(CHAMBRE_B_POS)
            chambre_b.nettoyer()
            self.derniere_chambre = "B"
            self.nettoyages += 1
            self.log("Nettoyage chambre B")



    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
