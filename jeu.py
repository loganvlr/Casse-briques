import pygame
import random
import math

pygame.init()

# ==================== Elements/Intéractions du jeu ====================

class Texte:
    """Classe permettant de créer un texte"""
    instances = []
    
    def __init__(self, texte, couleur, x = 0, y = 0):
        self.font = pygame.font.SysFont("consolas", 20)
        self.texte = texte
        self.couleur = couleur
        self.x = x
        self.y = y
        self.coor = (self.x, self.y)
        self.rendu = self.font.render(self.texte, True, self.couleur)
        Texte.instances.append(self)

    def __str__(self):
        return f"Texte({self.texte}, {self.couleur}, {self.x}, {self.y}, {self.coor})"
    
    def centrerLargeur(self, largeurConteneur, xConteneur = 0):
        self.x = (largeurConteneur / 2 - self.font.size(self.texte)[0] / 2) + xConteneur
        return self.x


    def centrerHauteur(self, hauteurConteneur, yConteneur = 0):
        self.y = (hauteurConteneur / 2 - self.font.size(self.texte)[1] / 2) + yConteneur
        return self.y

    
    def centrer(self, largeurConteneur = 0, hauteurConteneur = 0, xConteneur = 0, yConteneur = 0):
        if largeurConteneur > 0:
            self.x = self.centrerLargeur(largeurConteneur, xConteneur)
        
        if hauteurConteneur > 0:
            self.y = self.centrerHauteur(hauteurConteneur, yConteneur)
        self.coor = (self.x, self.y)
        return self




class Bouton:
    """Classe permettant de créer un bouton"""
    instances = []

    def __init__(self, nom, largeur, hauteur, couleur, x = 0, y = 0):
        self.nom = nom
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.x = x
        self.y = y
        self.coor = (self.x, self.y)
        self.rendu = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
        if self not in Bouton.instances:
            Bouton.instances.append(self)
    
    def __str__(self):
        return f"Bouton({self.largeur}, {self.hauteur}, {self.couleur}, {self.x}, {self.y}, {self.coor})"
    
    def centrerLargeur(self, largeurConteneur, xConteneur = 0):
        self.x = (largeurConteneur / 2 - self.largeur / 2) + xConteneur
        return self.x


    def centrerHauteur(self, hauteurConteneur, yConteneur = 0):
        self.y = (hauteurConteneur / 2 - self.hauteur / 2) + yConteneur
        return self.y

    
    def centrer(self, largeurConteneur = 0, hauteurConteneur = 0, xConteneur = 0, yConteneur = 0):
        if largeurConteneur > 0:
            self.x = self.centrerLargeur(largeurConteneur, xConteneur)
        
        if hauteurConteneur > 0:
            self.y = self.centrerHauteur(hauteurConteneur, yConteneur)
            
        self.rendu = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
        return self
        
    def isClicked(self, x, y):
        if x > self.x and x < self.x + self.largeur and y > self.y and y < self.y + self.hauteur:

            return True
        else:
            return False

    
    def get_page(self):
        # Retourne la classe correspondante en fonction du nom du bouton
        mapping = {
            "Accueil": Accueil,
            "Niveaux": Niveaux,
            "Options": Options,
            "Aide": Aide,
            "Scores": Scores,
            "Niveau1": 1,
            "Niveau2": 2,
            "Niveau3": 3,
        }
        if self.nom == "Quitter":
            exit(0)
        return mapping[self.nom]
    



# ==================== Pages (Une page est égal à une classe) ====================
class Accueil:

    def __init__(self):
        self.boutonJouer = Bouton("Niveaux", 200, 50, (125, 160, 202)).centrer(jeu.largeur, jeu.hauteur)
        self.texteJouer = Texte("Jouer", "white").centrer(self.boutonJouer.largeur, self.boutonJouer.hauteur, self.boutonJouer.x, self.boutonJouer.y)
        self.boutonOptions = Bouton("Options", 200, 50, (125, 160, 202)).centrer(jeu.largeur, jeu.hauteur, 0, 60)
        self.texteOptions = Texte("Options", "white").centrer(self.boutonOptions.largeur, self.boutonOptions.hauteur, self.boutonOptions.x, self.boutonOptions.y)
        self.boutonQuitter = Bouton("Quitter", 200, 50, (125, 160, 202)).centrer(jeu.largeur, jeu.hauteur, 0, 120)
        self.texteQuitter = Texte("Quitter", "white").centrer(self.boutonQuitter.largeur, self.boutonQuitter.hauteur, self.boutonQuitter.x, self.boutonQuitter.y)
        self.boutonAide = Bouton("Aide", 200, 50, (125, 160, 202)).centrer(jeu.largeur, jeu.hauteur, 0, 180)
        self.texteAide = Texte("Aide", "white").centrer(self.boutonAide.largeur, self.boutonAide.hauteur, self.boutonAide.x, self.boutonAide.y)
        self.boutonScores = Bouton("Scores", 200, 50, (125, 160, 202)).centrer(jeu.largeur, jeu.hauteur, 0, 240)
        self.texteScores = Texte("Scores", "white").centrer(self.boutonScores.largeur, self.boutonScores.hauteur, self.boutonScores.x, self.boutonScores.y)
        
        self.boutons = [self.boutonJouer, self.boutonOptions, self.boutonQuitter, self.boutonAide, self.boutonScores]
        self.textes = [self.texteJouer, self.texteOptions, self.texteQuitter, self.texteAide, self.texteScores]
    
    def click(self, x, y):
        boutons = self.boutons

        for bouton in boutons:
            if bouton.isClicked(x, y):
                page_classe = bouton.get_page()
                
                if page_classe is not None:
                    jeu.page = page_classe()

                return True
        return False
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.boutonJouer.couleur, self.boutonJouer.rendu, 0, 20)
        screen.blit(self.texteJouer.rendu, self.texteJouer.coor)

        pygame.draw.rect(screen, self.boutonOptions.couleur, self.boutonOptions.rendu, 0, 20)
        screen.blit(self.texteOptions.rendu, self.texteOptions.coor)
        
        pygame.draw.rect(screen, self.boutonQuitter.couleur, self.boutonQuitter.rendu, 0, 20)
        screen.blit(self.texteQuitter.rendu, self.texteQuitter.coor)
        
        pygame.draw.rect(screen, self.boutonAide.couleur, self.boutonAide.rendu, 0, 20)
        screen.blit(self.texteAide.rendu, self.texteAide.coor)
        
        pygame.draw.rect(screen, self.boutonScores.couleur, self.boutonScores.rendu, 0, 20)
        screen.blit(self.texteScores.rendu, self.texteScores.coor)

class Niveaux:
    
    def __init__(self):
        self.boutonNiveau1 = Bouton("Niveau1", 200, 50, (125, 160, 202)).centrer(jeu.largeur // 2, jeu.hauteur // 2)
        self.texteNiveau1 = Texte("Niveau 1", "white").centrer(self.boutonNiveau1.largeur, self.boutonNiveau1.hauteur, self.boutonNiveau1.x, self.boutonNiveau1.y)
        self.boutonNiveau2 = Bouton("Niveau2", 200, 50, (125, 160, 202)).centrer(jeu.largeur // 2, jeu.hauteur // 2, jeu.largeur // 2, 0)
        self.texteNiveau2 = Texte("Niveau 2", "white").centrer(self.boutonNiveau2.largeur, self.boutonNiveau2.hauteur, self.boutonNiveau2.x, self.boutonNiveau2.y)
        self.boutonNiveau3 = Bouton("Niveau3", 200, 50, (125, 160, 202)).centrer(jeu.largeur // 2, jeu.hauteur // 2, 0, jeu.hauteur // 2)
        self.texteNiveau3 = Texte("Niveau 3", "white").centrer(self.boutonNiveau3.largeur, self.boutonNiveau3.hauteur, self.boutonNiveau3.x, self.boutonNiveau3.y)
        self.boutonNiveauIA = Bouton("NiveauIA", 200, 50, (125, 160, 202)).centrer(jeu.largeur // 2, jeu.hauteur // 2, jeu.largeur // 2, jeu.hauteur // 2)
        self.texteNiveauIA = Texte("Niveau IA", "white").centrer(self.boutonNiveauIA.largeur, self.boutonNiveauIA.hauteur, self.boutonNiveauIA.x, self.boutonNiveauIA.y)
        self.boutonAccueil = Bouton("Accueil", 200, 50, (125, 160, 202)).centrer(jeu.largeur, jeu.hauteur)
        self.texteAccueil = Texte("Accueil", "white").centrer(self.boutonAccueil.largeur, self.boutonAccueil.hauteur, self.boutonAccueil.x, self.boutonAccueil.y)
        
        self.boutons = [self.boutonNiveau1, self.boutonNiveau2, self.boutonNiveau3, self.boutonNiveauIA, self.boutonAccueil]
        self.textes = [self.texteNiveau1, self.texteNiveau2, self.texteNiveau3, self.texteNiveauIA, self.texteAccueil]
    
    def click(self, x, y):
        boutons = self.boutons

        for bouton in boutons:
            if bouton.isClicked(x, y):
                page_classe = bouton.get_page()
                
                if page_classe is not None and not isinstance(page_classe, int):
                    jeu.page = page_classe()
                    
                elif page_classe == 1:
                    jeu.page = Niveau(5, 0, 0.08)
                
                elif page_classe == 2:
                    jeu.page = Niveau(6, 0.35, 0.08)
                
                elif page_classe == 3:
                    jeu.page = Niveau(7, 0.75, 0.08)
                return True
        return False
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.boutonNiveau1.couleur, self.boutonNiveau1.rendu, 0, 20)
        screen.blit(self.texteNiveau1.rendu, self.texteNiveau1.coor)
        
        pygame.draw.rect(screen, self.boutonNiveau2.couleur, self.boutonNiveau2.rendu, 0, 20)
        screen.blit(self.texteNiveau2.rendu, self.texteNiveau2.coor)
        
        pygame.draw.rect(screen, self.boutonNiveau3.couleur, self.boutonNiveau3.rendu, 0, 20)
        screen.blit(self.texteNiveau3.rendu, self.texteNiveau3.coor)
        
        pygame.draw.rect(screen, self.boutonNiveauIA.couleur, self.boutonNiveauIA.rendu, 0, 20)
        screen.blit(self.texteNiveauIA.rendu, self.texteNiveauIA.coor)
        
        pygame.draw.rect(screen, self.boutonAccueil.couleur, self.boutonAccueil.rendu, 0, 20)
        screen.blit(self.texteAccueil.rendu, self.texteAccueil.coor)

class Options:
    pass

class Aide:
    pass

class Scores:
    pass

class Brique:
    """Cette classe permet de créer une brique"""
    def __init__(self, x, y, hauteur, largeur, couleur, pourcentageBriquesModifie, pourcentageBonus):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.rendu = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
        if random.choices([True, False], weights = (pourcentageBriquesModifie, 1 - pourcentageBriquesModifie)) == [True]:
            self.vie = 2
        else:
            self.vie = 1
        
        if self.vie == 2:
            self.couleur = (0, 0, 0)
        else:
            self.couleur = couleur
            
        if random.choices([True, False], weights = (pourcentageBonus, 1 - pourcentageBonus)) == [True]:
            self.bonus = True
        else:
            self.bonus = False

class Plateforme:
    """Cette classe permet de créer une plateforme"""
    def __init__(self):
        
        self.largeur = int(jeu.largeur / 20) * 2.5
        self.hauteur = int((jeu.hauteur // 100) * 25 / 10) // 2
        self.x = jeu.largeur // 2 - self.largeur // 2
        self.y = jeu.hauteur - jeu.hauteur // 50 * 7.5
        self.rendu = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
        self.couleur = (0, 0, 0)
        self.bougeVersGauche = False
        self.bougeVersDroite = False

    def actualisation(self):
        self.rendu = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)

class Balle:
    def __init__(self):
        self.largeur = jeu.largeur / 128
        self.hauteur = self.largeur
        self.rayon = self.largeur // 2
        self.x = jeu.largeur // 2 - random.randint(-150, 150)
        self.y = jeu.hauteur - random.randint(jeu.hauteur // 50 * 5, jeu.hauteur - jeu.hauteur // 50 * 7)
        self.angle = random.uniform(math.pi * 0.75, math.pi * 1.25)
        self.couleur = (0, 0, 0)
        self.vitesse = jeu.hauteur / 72
    
    def rebond(self, axe):
        if axe == "horizontal":
            if self.angle == 180:
                self.angle = - self.angle + math.pi
            self.angle = -self.angle
        elif axe == "vertical":
            self.angle = math.pi - self.angle

    def rebondPlateforme(self, plateforme):
        print("plateforme")
        if plateforme.bougeVersGauche:
            self.angle = (math.pi - self.angle) - math.pi / 10
            
        elif plateforme.bougeVersDroite:
            self.angle = (math.pi - self.angle) + math.pi / 10
            
        else:
            self.angle = math.pi - self.angle
    
    def mouvements(self):
        self.x += math.sin(self.angle) * self.vitesse * -1
        self.y -= math.cos(self.angle) * self.vitesse * -1
        
class Niveau:
    
    
    def __init__(self, vitesseBalle, pourcentageBriquesModifie, pourcentageBonus):
        
        self.vitesseBalle = vitesseBalle
        self.vitesseRaquette = jeu.hauteur / 72
        self.pourcentageBriquesModifie = pourcentageBriquesModifie
        self.pourcentageBonus = pourcentageBonus
        self.briques = self.generationBriques(jeu.largeur, jeu.hauteur)
        self.plateforme = Plateforme()
        self.balle = Balle()
        self.score = 0
        self.boutonAccueil = Bouton("Accueil", 200, 50, (125, 160, 202)).centrer(jeu.largeur, jeu.hauteur)
        self.texteAccueil = Texte("Accueil", "white").centrer(self.boutonAccueil.largeur, self.boutonAccueil.hauteur, self.boutonAccueil.x, self.boutonAccueil.y)
        self.texteScore = Texte(f"Score : {self.score}", "black").centrer(largeurConteneur = jeu.largeur)
        
        self.boutons = [self.boutonAccueil]
        self.textes = [self.texteAccueil, self.texteScore]

    def click(self, x, y):
        boutons = self.boutons

        for bouton in boutons:
            if bouton.isClicked(x, y):
                page_classe = bouton.get_page()
                
                if page_classe is not None:
                    jeu.page = page_classe()
                return True
        return False
    
    def __str__(self):
        return f"Niveau({self.vitesseBalle}, {self.vitesseRaquette}, {self.pourcentageBriquesModifie}, {self.pourcentageBonus})"
    
    def generationBriques(self, largeurEcran, hauteurEcran):
        briques = []
        largeurBrique = int(largeurEcran / 20) # 20 correspond au nombre de briques par ligne

        hauteurMur = (hauteurEcran // 100) * 30 # 30 correspond à la hauteur du mur
        hauteurBrique = int(hauteurMur / 7) # 10 correspond au nombre de briques par colonne
        
        for x in range(0, largeurEcran, largeurBrique):
            for y in range(30, hauteurMur, hauteurBrique):
                briques.append(Brique(x, y, hauteurBrique, largeurBrique, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), self.pourcentageBriquesModifie, self.pourcentageBonus))
        return briques
    
    def collision(self, balle, plateforme, briques):
        self.collisionPlateforme(balle, plateforme)        
        self.collisionMur(balle)
        self.collisionBrique(balle)
    
    def collisionPlateforme(self, balle, plateforme):
        # Crée des rectangles pour la balle et la plateforme
        rect_balle = pygame.Rect(balle.x, balle.y, balle.rayon * 2, balle.rayon * 2)
        rect_plateforme = pygame.Rect(plateforme.x, plateforme.y, plateforme.largeur, plateforme.hauteur)

        # Vérifie si les rectangles se chevauchent
        if rect_balle.colliderect(rect_plateforme):
            # Gère le rebond et déplace la balle à l'extérieur de la plateforme
            balle.rebondPlateforme(plateforme)
            balle.y = rect_plateforme.top - balle.rayon * 2
    
    def collisionMur(self, balle):
        if balle.x <= 0 or balle.x + balle.rayon >= jeu.largeur:  # Si la balle a frappé un mur à gauche ou à droite
            balle.rebond("horizontal")


        if balle.y <= 0 or balle.y + balle.rayon >= jeu.hauteur:  # Si la balle a frappé un mur en haut ou en bas
            balle.rebond("vertical")
    
    def collisionBrique(self, balle):
        for brique in self.briques:
            # Crée des rectangles pour la balle et la brique
            rect_balle = pygame.Rect(balle.x, balle.y, balle.rayon * 2, balle.rayon * 2)
            rect_brique = pygame.Rect(brique.x, brique.y, brique.largeur, brique.hauteur)

            # Vérifie si les rectangles se chevauchent
            if rect_balle.colliderect(rect_brique):
                # Calcule les distances entre les côtés de la balle et de la brique
                distances = {
                    "gauche": abs(rect_balle.right - rect_brique.left),
                    "droite": abs(rect_balle.left - rect_brique.right),
                    "haut": abs(rect_balle.bottom - rect_brique.top),
                    "bas": abs(rect_balle.top - rect_brique.bottom)
                }

                # Détermine le côté de collision en fonction de la distance minimale
                cote_collision = min(distances, key=distances.get)

                # Gère le rebond et déplace la balle à l'extérieur de la brique
                if cote_collision in ["gauche", "droite"]:
                    balle.rebond("horizontal")
                    print("horizontal")
                    if cote_collision == "gauche":
                        print("gauche")
                        balle.x = rect_brique.left - balle.rayon * 2
                    else:
                        print("droite")
                        balle.x = rect_brique.right
                else:
                    balle.rebond("vertical")
                    print("vertical")
                    if cote_collision == "haut":
                        print("haut")
                        balle.y = rect_brique.top - balle.rayon * 2
                    else:
                        print("bas")
                        balle.y = rect_brique.bottom

                # Gère les vies de la brique
                if brique.vie == 1:
                    self.briques.remove(brique)
                    self.score = self.score + 10
                else:
                    brique.vie -= 1
                
                

                # Arrête de vérifier les autres briques
                break

                
            
    
    def draw(self, screen):

        pygame.draw.rect(screen, self.boutonAccueil.couleur, self.boutonAccueil.rendu, 0, 20)
        screen.blit(self.texteAccueil.rendu, self.texteAccueil.coor)
        
        self.texteScore.texte = f"Score : {self.score}"
        self.texteScore.rendu = self.texteScore.font.render(self.texteScore.texte, True, self.texteScore.couleur)
        screen.blit(self.texteScore.rendu, self.texteScore.coor)
        
        for brique in self.briques:
            pygame.draw.rect(screen, brique.couleur, brique.rendu, 0)
        
        self.plateforme.actualisation()
        self.balle.mouvements()
        self.collision(self.balle, self.plateforme, self.briques)
        
        pygame.draw.rect(screen, self.plateforme.couleur, self.plateforme.rendu, 0, 20)
        pygame.draw.circle(screen, self.balle.couleur, (self.balle.x, self.balle.y), self.balle.rayon * 2)
        

# ==================== Jeu ====================

class Jeu:
    def __init__(self):
        pygame.init()

        self.fps = 60
        self.FramePerSec = pygame.time.Clock()
        self.largeur = 1280
        self.hauteur = 720
        self.screen = pygame.display.set_mode((self.largeur, self.hauteur))
        self.running = True
        self.font = pygame.font.SysFont("consolas", 20)
        

    def run(self):
        self.page = Accueil()
        while self.running:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # ==================== Event detection ====================
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                    
            # ==================== Update ====================
            self.screen.fill("white")
            self.FramePerSec.tick(self.fps) # 60 FPS limit
            self.page.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.page.click(mouse_x, mouse_y)

            if isinstance(self.page, Niveau):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] and self.page.plateforme.x > 5:
                    self.page.plateforme.x -= self.page.vitesseRaquette
                if keys[pygame.K_LEFT]:
                    self.page.plateforme.bougeVersGauche = True
                else:
                    self.page.plateforme.bougeVersGauche = False
                    
                if keys[pygame.K_RIGHT] and self.page.plateforme.x + self.page.plateforme.largeur < self.largeur - 5:
                    self.page.plateforme.x += self.page.vitesseRaquette
                    
                if keys[pygame.K_RIGHT]:
                    self.page.plateforme.bougeVersDroite = True
                else:
                    self.page.plateforme.bougeVersDroite = False
                    
            pygame.display.flip()

jeu = Jeu()
jeu.run()