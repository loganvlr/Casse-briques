import pygame
import random
import math

class Boutons:
    def __init__(self, fenetre, texte, x, y, largeur, hauteur, couleur = (255, 255, 255), couleur_texte = (0, 0, 0), largeur_cote = 0, arrondissements_bords = 0, arrondissement_haut_gauche = 0, arrondissement_haut_droit = 0, arrondissement_bas_gauche = 0, arrondissement_bas_droit = 0, action = None, page = None) -> None:
        """Cette méthode permet d'initialiser un bouton

        Args:
            fenetre (pygame.Surface): fenêtre du jeu
            texte (str): texte du bouton
            x (int): position en x du bouton
            y (int): position en y du bouton
            largeur (int): largeur en pixels (px) du bouton
            hauteur (int): hauteur en pixels (px) du bouton
            couleur (tuple, optional): couleur du bouton. Defaults to (255, 255, 255).
            couleur_texte (tuple, optional): couleur du texte du bouton. Defaults to (0, 0, 0).
            arrondissements_bords (int, optional): arrondissements des bords du bouton. Defaults to 0.
            action (fonction, optional): action du bouton. Defaults to None.
            page (Page, optional): page que représente le bouton. Defaults to None.
        """
        self.fenetre = fenetre
        self.texte = jeu.police.render(texte, True, couleur_texte)
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur_origine = couleur
        self.couleur = couleur
        self.couleur_texte = couleur_texte
        self.largeur_cote = largeur_cote
        self.arrondissements_bords = arrondissements_bords
        self.arrondissement_haut_gauche = arrondissement_haut_gauche
        self.arrondissement_haut_droit = arrondissement_haut_droit
        self.arrondissement_bas_gauche = arrondissement_bas_gauche
        self.arrondissement_bas_droit = arrondissement_bas_droit
        self.action = action
        self.page = page
        self.rendu =  pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
    
    def afficher(self, fenetre):
        """Cette méthode permet d'afficher le bouton à l'écran
        """
        pygame.draw.rect(fenetre, self.couleur, self.rendu, width = self.largeur_cote , border_radius = self.arrondissements_bords, border_top_left_radius = self.arrondissement_haut_gauche, border_top_right_radius = self.arrondissement_haut_droit, border_bottom_left_radius = self.arrondissement_bas_gauche, border_bottom_right_radius = self.arrondissement_bas_droit)
        fenetre.blit(self.texte, (self.x + (self.largeur / 2 - self.texte.get_width() / 2), self.y + (self.hauteur / 2 - self.texte.get_height() / 2)))
    
    def survoler(self):
        """Cette méthode permet de savoir si le bouton est survolé par la souris

        Returns:
            bool: True si le bouton est survolé, False sinon
        """
        if self.x < pygame.mouse.get_pos()[0] < self.x + self.largeur and self.y < pygame.mouse.get_pos()[1] < self.y + self.hauteur:
            return True
        return False
    
    def cliquer(self):
        """Cette méthode permet de savoir si le bouton est cliqué

        Returns:
            bool: True si le bouton est cliqué, False sinon
        """
        if self.survoler() and pygame.mouse.get_pressed()[0]:
            if self.page != None:
                jeu.page = self.page()
            elif self.action != None:
                if self.action == "Quitter":
                    self.quitter()
    
    def quitter(self):
        """Cette méthode permet de quitter le jeu
        """
        jeu.executer = False

    def centrerLargeur(self, largeurConteneur, xConteneur = 0):
        """Cette méthode permet de centrer un bouton en largeur par rapport à un conteneur. Le conteneur peu être n'importe où dans la fenêtre.
        Args:
            largeurConteneur(int): largeur du conteneur dans lequel on veut centrer le contenu.
            xConteneur(int or float): position x du conteneur si celui-ci est décalé par rapport au bord de la fenêtre.
        Return:
            (float): position x du bouton qui permettra de centrer celui-ci dans le conteneur.
        """
        self.x = (largeurConteneur / 2 - self.largeur / 2) + xConteneur
        return self.x


    def centrerHauteur(self, hauteurConteneur, yConteneur = 0):
        """Cette méthode permet de centrer un bouton en hauteur par rapport à un conteneur. Le conteneur peu être n'importe où dans la fenêtre.
        Args:
            largeurConteneur(int): hauteur du conteneur dans lequel on veut centrer le contenu.
            xConteneur(int or float): position y du conteneur si celui-ci est décalé par rapport au bord de la fenêtre.
        Return:
            (float): position y du bouton qui permettra de centrer celui-ci dans le conteneur.
        """
        self.y = (hauteurConteneur / 2 - self.hauteur / 2) + yConteneur
        return self.y
    
    def centrer(self, largeurConteneur = 0, hauteurConteneur = 0, xConteneur = 0, yConteneur = 0):
        """Cette méthode permet de centrer un bouton en largeur ou en hauteur ou les deux à la fois par rapport à un conteneur. Le conteneur peu être n'importe où dans la fenêtre.
        Args:
            largeurConteneur(int or float): largeur du conteneur dans lequel on veut centrer le contenu.
            hauteurConteneur(int or float): largeur du conteneur dans lequel on veut centrer le contenu.
            xConteneur(int or float):  position x du conteneur si celui-ci est décalé par rapport au bord de la fenêtre.
            yConteneur(int or float):  position y du conteneur si celui-ci est décalé par rapport au bord de la fenêtre.
        Return:
            (Bouton): on retourne le bouton
        """
        if largeurConteneur > 0:
            self.x = self.centrerLargeur(largeurConteneur, xConteneur)
        
        if hauteurConteneur > 0:
            self.y = self.centrerHauteur(hauteurConteneur, yConteneur)
            
        self.rendu = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
        return self





class BoutonsAvecOmbre(Boutons):
    def __init__(self, fenetre, texte, x, y, largeur, hauteur, couleur=(255, 255, 255), couleur_texte=(0, 0, 0),
                 largeur_cote=0, arrondissements_bords=0, arrondissement_haut_gauche=0,
                 arrondissement_haut_droit=0, arrondissement_bas_gauche=0, arrondissement_bas_droit=0,
                 action=None, page=None, ombre_offset=5, ombre_couleur=(255, 255, 255)) -> None:
        super().__init__(fenetre, texte, x, y, largeur, hauteur, couleur, couleur_texte, largeur_cote,
                         arrondissements_bords, arrondissement_haut_gauche, arrondissement_haut_droit,
                         arrondissement_bas_gauche, arrondissement_bas_droit, action, page)

        self.ombre_offset = ombre_offset
        self.ombre_couleur = ombre_couleur

    def afficher(self, fenetre):
        # Dessiner l'ombre
        ombre_rect = pygame.Rect(self.x, self.y + self.ombre_offset,
                                 self.largeur, self.hauteur)
        pygame.draw.rect(fenetre, self.ombre_couleur, ombre_rect, width=self.largeur_cote,
                         border_radius=self.arrondissements_bords,
                         border_top_left_radius=self.arrondissement_haut_gauche,
                         border_top_right_radius=self.arrondissement_haut_droit,
                         border_bottom_left_radius=self.arrondissement_bas_gauche,
                         border_bottom_right_radius=self.arrondissement_bas_droit)

        # Appeler la méthode d'affichage de la classe parente
        super().afficher(fenetre)





class Page:
    def __init__(self) -> None:
        pass
    
    def afficher(self):
        for bouton in self.boutons:
            bouton.afficher(jeu.fenetre)

class Accueil(Page):
    def __init__(self) -> None:
        self.boutonJouer = BoutonsAvecOmbre(jeu.fenetre, "Jouer", 100, 100, 350, 80, (150, 178, 233), (255, 255, 255),
                                           arrondissement_haut_gauche=10, arrondissement_haut_droit=10,
                                           arrondissement_bas_gauche=35, arrondissement_bas_droit=35,
                                           page = Niveaux).centrer(jeu.largeur, jeu.hauteur)
        
        self.boutonOptions = BoutonsAvecOmbre(jeu.fenetre, "Options", 100, 100, 350, 80, (150, 178, 233), (255, 255, 255),
                                     arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10,
                                     arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35,
                                     page = Options).centrer(jeu.largeur, jeu.hauteur, 0, 95)
        
        self.boutonAide = BoutonsAvecOmbre(jeu.fenetre, "Aide", 100, 100, 350, 80, (150, 178, 233), (255, 255, 255),
                                  arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10,
                                  arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35).centrer(jeu.largeur, jeu.hauteur, 0, 190)
        
        self.boutonScores = BoutonsAvecOmbre(jeu.fenetre, "Scores", 100, 100, 350, 80, (150, 178, 233), (255, 255, 255),
                                    arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10,
                                    arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35).centrer(jeu.largeur, jeu.hauteur, 0, 285)
        
        self.boutonQuitter = BoutonsAvecOmbre(jeu.fenetre, "Quitter", 100, 100, 350, 80, (150, 178, 233), (255, 255, 255),
                                     arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10,
                                     arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35,
                                     action = "Quitter").centrer(jeu.largeur, jeu.hauteur, 0, 380)
        
        self.boutons = [self.boutonJouer, self.boutonOptions, self.boutonAide, self.boutonScores, self.boutonQuitter]

class Niveaux(Page):
    def __init__(self) -> None:
        self.boutonAccueil = Boutons(jeu.fenetre, "Accueil", 100, 100, 200, 100, (150, 178, 233), (255, 255, 255), 10, page = Accueil).centrer(jeu.largeur, jeu.hauteur)
        
        self.boutons = [self.boutonAccueil]

class Options(Page):
    def __init__(self) -> None:
        self.boutonTest2 = Boutons(jeu.fenetre, "Accueil", 100, 100, 200, 100, (150, 178, 233), (255, 255, 255), 10, page = Accueil).centrer(jeu.largeur, jeu.hauteur)
        
        self.boutons = [self.boutonTest2]

class Aide(Page):
    pass

class Scores(Page):
    pass


class Jeu:
    def __init__(self) -> None:
        pygame.init()
        self.fps = 60
        
        self.largeur = 1920
        self.hauteur = 1080
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        
        self.police = pygame.font.SysFont("Arial", 30)
        self.executer = True
        
        
        self.image = pygame.image.load("img/fond_blanc.jpg").convert()
        self.image = pygame.transform.scale(self.image, (self.largeur, self.hauteur))
        
    
    def gerer_evenements(self):
        """Cette méthode permet de gérer les événements du jeu
        """
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                self.executer = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                for bouton in self.page.boutons:
                    bouton.cliquer()
        
        # Si le bouton est survolé, il change de couleur
        for bouton in self.page.boutons:
                if bouton.survoler():
                    bouton.couleur = (198, 198, 233)
                else:
                    bouton.couleur = bouton.couleur_origine
    
    def executer_jeu(self):
        """Cette méthode permet d'exécuter le jeu
        """
        self.page = Accueil()
        while self.executer:
            self.fenetre.fill((255, 255, 255))
            self.fenetre.blit(self.image, (0, 0)) # A étudier
            self.page.afficher()
            self.gerer_evenements()
            pygame.display.flip()


jeu = Jeu()
jeu.executer_jeu()