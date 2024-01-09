import pygame
import random
import math

class Flexbox:
    def __init__(self, elements, largeur, hauteur, x = 0, y = 0, flex_direction = "row", justify_content = "flex-start", align_content = "flex-start", taux_espace_justify = 0, taux_espace_align = 0, centrer_largeur = False, centrer_hauteur = False) -> None:
        """ Cette méthode permet d'initialiser une flexbox
        Args:
            elements (list): liste des éléments de la flexbox
            largeur (int or float): largeur de la flexbox
            hauteur (int or float): hauteur de la flexbox
            x (int or float, optional): position x de la flexbox. Defaults to 0.
            y (int or float, optional): position y de la flexbox. Defaults to 0.
            flex_direction (str, optional): direction de la flexbox. Defaults to "row".
            justify_content (str, optional): alignement horizontal des éléments de la flexbox. Defaults to "flex-start".
            align_content (str, optional): alignement vertical des éléments de la flexbox. Defaults to "flex-start".
            taux_espace_justify (int or float, optional): taux d'espace entre les éléments de la flexbox. Defaults to 0.
            taux_espace_align (int or float, optional): taux d'espace entre les éléments de la flexbox. Defaults to 0.
            centrer_largeur (bool, optional): centrer la flexbox en largeur. Defaults to False.
            centrer_hauteur (bool, optional): centrer la flexbox en hauteur. Defaults to False.
        """
        self.nb_elements = len(elements)
        self.elements = elements
        self.flex_direction = flex_direction
        self.justify_content = justify_content
        self.align_content = align_content
        self.taux_espace_justify = taux_espace_justify
        self.taux_espace_align = taux_espace_align

        
        # Définir la largeur et la hauteur de la flexbox
        if largeur <= 1: # Si la largeur est inférieure ou égale à 1, on la multiplie par la largeur de la fenêtre (c'est un pourcentage)
            self.largeur = largeur * jeu.largeur
        else:
            self.largeur = largeur
        if hauteur <= 1:
            self.hauteur = hauteur * jeu.hauteur
        else:
            self.hauteur = hauteur
        
        
        # Définir la position de la flexbox
        if not centrer_largeur and not centrer_hauteur:
            if x <= 1:
                self.x = x * jeu.largeur
            else:
                self.x = x
            if y <= 1:
                self.y = y * jeu.hauteur
            else:
                self.y = y
            
        elif centrer_largeur and not centrer_hauteur:
            self.x = self.centrerLargeur()
            if y <= 1:
                self.y = y * jeu.hauteur
            else:
                self.y = y
                
        elif not centrer_largeur and centrer_hauteur:
            if x <= 1:
                self.x = x * jeu.largeur
            else:
                self.x = x
            self.y = self.centrerHauteur()
            
        else:
            self.centrer(centrer_largeur, centrer_hauteur)
        
        
        
        # Définir la largeur des éléments
        if self.justify_content == "space-between":
            self.justify_space_between()
            
        elif self.flex_direction == "column":
            largeur = self.largeur
            for element in self.elements:
                element.largeur = largeur
                element.x = self.x
                
        elif self.flex_direction == "row":
            largeur = self.largeur / self.nb_elements
            for num, element in enumerate(self.elements):
                element.largeur = largeur
                element.x = self.x + (element.largeur * num)
        
        # Définir la hauteur des éléments
        if self.align_content == "space-between":
            self.align_space_between()
            
        elif flex_direction == "column":
            hauteur = self.hauteur / self.nb_elements
            for num, element in enumerate(self.elements):
                element.hauteur = hauteur
                element.y = self.y + (element.hauteur * num)
                
        elif flex_direction == "row":
            hauteur = self.hauteur
            for element in self.elements:
                element.hauteur = hauteur
                element.y = self.y
        
        for element in self.elements:
            element.x_origine = element.x
            element.y_origine = element.y
    
    def justify_space_between(self):
        """ Cette méthode permet de placer les éléments de la flexbox avec un espace entre eux en largeur
        """
        nb_espaces = self.nb_elements - 1
        
        # Calculer l'espace entre les éléments
        total_espace = self.largeur * self.taux_espace_justify
        espace = total_espace / nb_espaces

        # Calculer la largeur des éléments
        largeur_elements = self.largeur - total_espace
        largeur = largeur_elements / self.nb_elements

        # Placer les éléments
        for num, element in enumerate(self.elements):
            element.largeur = largeur
            element.x = self.x + (element.largeur * num) + (espace * num)
    
    def align_space_between(self):
        """ Cette méthode permet de placer les éléments de la flexbox avec un espace entre eux en hauteur
        """
        nb_espaces = self.nb_elements - 1
        
        # Calculer l'espace entre les éléments
        total_espace = self.hauteur * self.taux_espace_align
        espace = total_espace / nb_espaces

        # Calculer la hauteur des éléments
        hauteur_elements = self.hauteur - total_espace
        hauteur = hauteur_elements / self.nb_elements

        # Placer les éléments
        for num, element in enumerate(self.elements):
            element.hauteur = hauteur
            element.y = self.y + (element.hauteur * num) + (espace * num)
    
    def centrerLargeur(self):
        return jeu.largeur / 2 - self.largeur / 2
    
    def centrerHauteur(self):
        return jeu.hauteur / 2 - self.hauteur / 2
    
    def centrer(self, largeur = False, hauteur = False):
        print("centrer")
        if largeur:
            self.x = self.centrerLargeur()
        if hauteur:
            self.y = self.centrerHauteur()
        return self




class Boutons:
    def __init__(self, fenetre, texte, x, y, largeur, hauteur, couleur = (255, 255, 255), couleur_texte = (0, 0, 0), largeur_cote = 0, arrondissements_bords = 0, arrondissement_haut_gauche = 0, arrondissement_haut_droit = 0, arrondissement_bas_gauche = 0, arrondissement_bas_droit = 0, action = None, page = None, ombre_offset=5, ombre_couleur=(255, 255, 255)) -> None:
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
        # Fenêtre
        self.fenetre = fenetre
        
        # Texte
        self.texte = jeu.police.render(texte, True, couleur_texte)
        
        # Coordonnées
        self.x = x
        self.y = y
        self.x_origine = x
        self.y_origine = y
        
        # Dimensions
        self.largeur = largeur
        self.hauteur = hauteur
        self.largeur_cote = largeur_cote
        
        # Couleurs
        self.couleur_origine = couleur
        self.couleur = couleur
        self.couleur_texte = couleur_texte
        
        # Arrondissements
        self.arrondissements_bords = arrondissements_bords
        self.arrondissement_haut_gauche = arrondissement_haut_gauche
        self.arrondissement_haut_droit = arrondissement_haut_droit
        self.arrondissement_bas_gauche = arrondissement_bas_gauche
        self.arrondissement_bas_droit = arrondissement_bas_droit
        
        # Action
        self.action = action
        self.page = page
        
        # Ombre
        self.ombre_offset = ombre_offset
        self.ombre_couleur = ombre_couleur
        self.ombre = True
        
    
    def afficher(self, fenetre):
        """Cette méthode permet d'afficher le bouton à l'écran
        """
        # Dessiner l'ombre
        if self.ombre:
            ombre_rect = pygame.Rect(self.x, self.y + self.ombre_offset,
                                    self.largeur, self.hauteur)
            pygame.draw.rect(fenetre, self.ombre_couleur, ombre_rect, self.largeur_cote,
                            self.arrondissements_bords,
                            self.arrondissement_haut_gauche,
                            self.arrondissement_haut_droit,
                            self.arrondissement_bas_gauche,
                            self.arrondissement_bas_droit)
        
        # Dessiner le bouton
        self.rendu =  pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
        pygame.draw.rect(fenetre, self.couleur, self.rendu, self.largeur_cote,
                        self.arrondissements_bords,
                        self.arrondissement_haut_gauche,
                        self.arrondissement_haut_droit,
                        self.arrondissement_bas_gauche,
                        self.arrondissement_bas_droit)
        
        # Dessiner le texte
        fenetre.blit(self.texte, (self.x + (self.largeur / 2 - self.texte.get_width() / 2), self.y + (self.hauteur / 2 - self.texte.get_height() / 2)))

        if not self.ombre:
            encadrement_rect = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
            pygame.draw.rect(fenetre, self.ombre_couleur, encadrement_rect, self.ombre_offset,
                            self.arrondissements_bords,
                            self.arrondissement_haut_gauche,
                            self.arrondissement_haut_droit,
                            self.arrondissement_bas_gauche,
                            self.arrondissement_bas_droit)
        
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




class Page:
    def __init__(self) -> None:
        pass
    
    def afficher(self):
        for bouton in self.boutons:
            bouton.afficher(jeu.fenetre)

class Accueil(Page):
    def __init__(self) -> None:
        self.boutonJouer = Boutons(jeu.fenetre, "Jouer", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255),
                                           arrondissement_haut_gauche=10, arrondissement_haut_droit=10,
                                           arrondissement_bas_gauche=35, arrondissement_bas_droit=35,
                                           page = Niveaux)
        
        self.boutonOptions = Boutons(jeu.fenetre, "Options", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255),
                                     arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10,
                                     arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35,
                                     page = Options)
        
        self.boutonAide = Boutons(jeu.fenetre, "Aide", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255),
                                  arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10,
                                  arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35)
        
        self.boutonScores = Boutons(jeu.fenetre, "Scores", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255),
                                    arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10,
                                    arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35)
        
        self.boutonQuitter = Boutons(jeu.fenetre, "Quitter", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255),
                                     arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10,
                                     arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35,
                                     action = "Quitter")
        
        self.boutons = [self.boutonJouer, self.boutonOptions, self.boutonAide, self.boutonScores, self.boutonQuitter]
        menu = Flexbox(self.boutons, 0.20, 0.45, flex_direction="column", align_content="space-between", taux_espace_align=0.1, centrer_largeur=True, y = 0.45)
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
        
        self.largeur = 2560# 3840
        self.hauteur = 1440# 2160
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        
        self.police = pygame.font.SysFont("Arial", 30)
        self.executer = True
        
        
        self.image = pygame.image.load("img/Menu.jpg").convert()
        self.image = pygame.transform.scale_by(self.image, (self.largeur / self.image.get_width()))
        
        self.position_souris = pygame.mouse.get_pos()
    
    def gerer_evenements(self):
        """Cette méthode permet de gérer les événements du jeu
        """
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                self.executer = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                for bouton in self.page.boutons:
                    bouton.cliquer()
        
        # Cette condition permet de savoir si la souris a bougé, et donc de ne pas faire des calculs inutiles
        position_souris_temp = pygame.mouse.get_pos()
        if position_souris_temp != self.position_souris:
            self.position_souris = position_souris_temp
            
            # Si le bouton est survolé, il change de couleur et s'enfonce
            for bouton in self.page.boutons:
                    if bouton.survoler():
                        bouton.couleur = (90, 90, 90)
                        if bouton.action == "Quitter":
                            bouton.couleur = (255, 0, 0)
                        bouton.y = bouton.y_origine + bouton.ombre_offset
                        bouton.ombre = False
                    
                    # Sinon, il reprend sa couleur d'origine et remonte
                    else:
                        bouton.couleur = bouton.couleur_origine
                        bouton.y = bouton.y_origine
                        bouton.ombre = True
    
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