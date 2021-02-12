import pygame
pygame.init()

# Generation de  la fenetre du Jeu
pygame.display.set_caption("Le Quiz de EMCI TV")
pygame.display.set_mode((1080, 720))

# Jeu actif tant que la variable est active
running = True

# Boucle du jeu
while running:

    # fermeture de la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Femeture du jeu")
        elif event.type == pygame.KEYDOWN:
            print("clavier validé")
            if event.type == pygame.K_a:
                print("Action choix A")
            elif event.type == pygame.K_b:
                 print("Action choix B")
            elif event.type == pygame.K_c:
                print("Action choix C")
            elif event.type == pygame.K_d:
                print("Action choix D")
            elif event.type == pygame.K_p:
                print("Action choix Pause")
            elif event.type == pygame.K_q:
                print("Action choix Quitter")
            elif event.type == pygame.K_w:
                print("Action choix Continuer")
            elif event.type == pygame.K_s:
                print("Action choix Skip")
        elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Souris validé")


# Integration de la Logique du jeu

# Suppression du champ de Jeu

# Champs de Jeu

# Actualisation de la fenetre du jeu
pygame.display.flip()

# Periode de rafraichissement de la page
clock = pygame.time.Clock()
clock.tick(60)