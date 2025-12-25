import pygame
import time
import random

from config import *
from environment import Chambre
from agent import AgentAspirateur

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TP1 - Agent Intelligent Aspirateur")

font = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()

# Chambres
chambre_a = Chambre("A", CHAMBRE_A_POS)
chambre_b = Chambre("B", CHAMBRE_B_POS)

# Agent
agent = AgentAspirateur("assets/aspirateur.png")

dernier_passage = time.time()
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logique temporelle
    if time.time() - dernier_passage >= INTERVALLE_NETTOYAGE:
        agent.agir(chambre_a, chambre_b)

        # Re-salir aléatoirement
        chambre_a.sale = random.choice([True, False])
        chambre_b.sale = random.choice([True, False])

        dernier_passage = time.time()

    # Dessins
    chambre_a.draw(screen, font)
    chambre_b.draw(screen, font)
    agent.draw(screen)

    # Infos écran
    compteur = font.render(f"Nettoyages : {agent.nettoyages}", True, BLACK)
    screen.blit(compteur, (10, 10))

    y_log = 300
    for log in agent.logs:
        txt = font.render(log, True, BLACK)
        screen.blit(txt, (10, y_log))
        y_log += 20

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
