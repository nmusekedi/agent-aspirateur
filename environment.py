import pygame
from config import *

class Chambre:
    def __init__(self, nom, position):
        self.nom = nom
        self.position = position
        self.sale = True

    def nettoyer(self):
        self.sale = False

    def salir(self):
        self.sale = True

    def draw(self, screen, font):
        couleur = RED if self.sale else GREEN
        pygame.draw.rect(
            screen,
            couleur,
            (*self.position, *CHAMBRE_SIZE)
        )

        titre = font.render(f"Chambre {self.nom}", True, BLACK)
        etat = font.render("SALE" if self.sale else "PROPRE", True, BLACK)

        screen.blit(titre, (self.position[0] + 30, self.position[1] + 60))
        screen.blit(etat, (self.position[0] + 40, self.position[1] + 100))
