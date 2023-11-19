import pygame
import random

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
        self.boutonJouer = Bouton("Niveaux", 200, 50, (125, 160, 202)).centrer(1280, 720)
        self.texteJouer = Texte("Jouer", "white").centrer(self.boutonJouer.largeur, self.boutonJouer.hauteur, self.boutonJouer.x, self.boutonJouer.y)
        self.boutonOptions = Bouton("Options", 200, 50, (125, 160, 202)).centrer(1280, 720, 0, 60)
        self.texteOptions = Texte("Options", "white").centrer(self.boutonOptions.largeur, self.boutonOptions.hauteur, self.boutonOptions.x, self.boutonOptions.y)
        self.boutonQuitter = Bouton("Quitter", 200, 50, (125, 160, 202)).centrer(1280, 720, 0, 120)
        self.texteQuitter = Texte("Quitter", "white").centrer(self.boutonQuitter.largeur, self.boutonQuitter.hauteur, self.boutonQuitter.x, self.boutonQuitter.y)
        self.boutonAide = Bouton("Aide", 200, 50, (125, 160, 202)).centrer(1280, 720, 0, 180)
        self.texteAide = Texte("Aide", "white").centrer(self.boutonAide.largeur, self.boutonAide.hauteur, self.boutonAide.x, self.boutonAide.y)
        self.boutonScores = Bouton("Scores", 200, 50, (125, 160, 202)).centrer(1280, 720, 0, 240)
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
    
    def actualisation(self):
        self.rendu = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
class Niveau:
    
    
    def __init__(self, vitesseBalle, pourcentageBriquesModifie, pourcentageBonus):
        
        self.vitesseBalle = vitesseBalle
        self.vitesseRaquette = 15
        self.pourcentageBriquesModifie = pourcentageBriquesModifie
        self.pourcentageBonus = pourcentageBonus
        self.briques = self.generationBriques(jeu.largeur, jeu.hauteur)
        self.plateforme = Plateforme()
        
        self.boutonAccueil = Bouton("Accueil", 200, 50, (125, 160, 202)).centrer(jeu.largeur, jeu.hauteur)
        self.texteAccueil = Texte("Accueil", "white").centrer(self.boutonAccueil.largeur, self.boutonAccueil.hauteur, self.boutonAccueil.x, self.boutonAccueil.y)
        
        self.boutons = [self.boutonAccueil]
        self.textes = [self.texteAccueil]

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

        hauteurMur = (hauteurEcran // 100) * 25 # 20 correspond à la hauteur du mur
        hauteurBrique = int(hauteurMur / 10) # 10 correspond au nombre de briques par colonne
        
        for x in range(0, largeurEcran, largeurBrique):
            for y in range(30, hauteurMur, hauteurBrique):
                briques.append(Brique(x, y, hauteurBrique, largeurBrique, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), self.pourcentageBriquesModifie, self.pourcentageBonus))
        return briques
    
    def draw(self, screen):

        pygame.draw.rect(screen, self.boutonAccueil.couleur, self.boutonAccueil.rendu, 0, 20)
        screen.blit(self.texteAccueil.rendu, self.texteAccueil.coor)
        
        for brique in self.briques:
            pygame.draw.rect(screen, brique.couleur, brique.rendu, 0, 7)
        
        
        self.plateforme.actualisation()
        pygame.draw.rect(screen, self.plateforme.couleur, self.plateforme.rendu, 0, 20)
        

# ==================== Jeu ====================

class Jeu:
    def __init__(self):
        pygame.init()

        self.fps = 60
        self.FramePerSec = pygame.time.Clock()
        self.largeur = 1920
        self.hauteur = 1080
        self.screen = pygame.display.set_mode((self.largeur, self.hauteur))
        self.running = True
        self.font = pygame.font.SysFont("consolas", 20)
        self.page = Accueil()

    def run(self):
        while self.running:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # ==================== Event detection ====================
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                    
            # ==================== Update ====================
            self.screen.fill("white")
            self.FramePerSec.tick(60) # 60 FPS limit
            self.page.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.page.click(mouse_x, mouse_y)

            if isinstance(self.page, Niveau):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.page.plateforme.x -= self.page.vitesseRaquette
                    
                if keys[pygame.K_RIGHT]:
                    self.page.plateforme.x += self.page.vitesseRaquette
                        
            pygame.display.flip()

jeu = Jeu()
jeu.run()