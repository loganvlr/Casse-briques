import pygame
import random
import math
from math import pi, sqrt

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
            if isinstance(element, Flexbox):
                element = Flexbox(element.elements, element.largeur, element.hauteur, element.x, element.y, element.flex_direction, element.justify_content, element.align_content, element.taux_espace_justify, element.taux_espace_align)
    
    def justify_space_between(self):
        """ Cette méthode permet de placer les éléments de la flexbox avec un espace entre eux en largeur
        """
        nb_espaces = self.nb_elements - 1
        
        # Calculer l'espace entre les éléments
        total_espace = self.largeur * self.taux_espace_justify
        if nb_espaces > 0:
            espace = total_espace / nb_espaces
        else:
            espace = 0

        # Calculer la largeur des éléments
        largeur_elements = self.largeur - total_espace
        largeur = largeur_elements / self.nb_elements

        # Placer les éléments
        for num, element in enumerate(self.elements):
            element.largeur = largeur
            element.x = self.x + (element.largeur * num) + (espace * num)
            
            # Pour actualiser le rendu de l'élément (à revoir ?)
            if isinstance(element, Brique):
                element.rendu = pygame.Rect(element.x, element.y, element.largeur, element.hauteur)
    
    def align_space_between(self):
        """ Cette méthode permet de placer les éléments de la flexbox avec un espace entre eux en hauteur
        """
        nb_espaces = self.nb_elements - 1
        
        # Calculer l'espace entre les éléments
        total_espace = self.hauteur * self.taux_espace_align
        if nb_espaces > 0:
            
            espace = total_espace / nb_espaces
        else:
            espace = 0

        # Calculer la hauteur des éléments
        if nb_espaces > 0:
            hauteur_elements = self.hauteur - total_espace
            hauteur = hauteur_elements / self.nb_elements
        else:
            hauteur = self.hauteur

        # Placer les éléments
        for num, element in enumerate(self.elements):
            element.hauteur = hauteur
            element.y = self.y + (element.hauteur * num) + (espace * num)
            # Pour actualiser le rendu de l'élément (à revoir ?)
            if isinstance(element, Brique):
                element.rendu = pygame.Rect(element.x, element.y, element.largeur, element.hauteur)
    
    def centrerLargeur(self):
        return jeu.largeur / 2 - self.largeur / 2
    
    def centrerHauteur(self):
        return jeu.hauteur / 2 - self.hauteur / 2
    
    def centrer(self, largeur = False, hauteur = False):
        if largeur:
            self.x = self.centrerLargeur()
        if hauteur:
            self.y = self.centrerHauteur()
        return self

class Texte:
    def __init__(self, texte, couleur, x, y, largeur, hauteur, taille = None) -> None:
        """Cette méthode permet d'initialiser un texte

        Args:
            texte (str): texte du texte
            couleur (tuple): couleur du texte
            x (int or float): position en x du texte
            y (int or float): position en y du texte
            largeur (int or float): largeur du texte
            hauteur (int or float): hauteur du texte
            police (str, optional): police du texte. Defaults to None.
            taille (int, optional): taille du texte. Defaults to 0.
            centrer (bool, optional): centrer le texte. Defaults to False.
            centrer_largeur (bool, optional): centrer le texte en largeur. Defaults to False.
            centrer_hauteur (bool, optional): centrer le texte en hauteur. Defaults to False.
        """
        # Police
        self.taille = taille
        
        if self.taille is None:
            font = jeu.police
        else:
            font = pygame.font.Font(jeu.policeOrig, self.taille)
        
        
        # Texte
        self.texte = font.render(texte, True, couleur)
        
        # Coordonnées
        self.x = x
        self.y = y
        
        # Dimensions
        self.largeur = largeur
        self.hauteur = hauteur
        
        # Rendu
        self.rendu = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
    
    def afficher(self):
        """Cette méthode permet d'afficher le texte à l'écran
        """
        jeu.fenetre.blit(self.texte, (self.x + (self.largeur / 2 - (self.texte.get_width() / 2)), self.y + (self.hauteur / 2 - (self.texte.get_height() / 2))))


class Boutons:
    def __init__(self, fenetre, texte, x, y, largeur, hauteur, couleur = (255, 255, 255), couleur_texte = (0, 0, 0), largeur_cote = 0, arrondissements_bords = 0, arrondissement_haut_gauche = 0, arrondissement_haut_droit = 0, arrondissement_bas_gauche = 0, arrondissement_bas_droit = 0, action = None, page = None, ombre_offset=5, ombre_couleur=(255, 255, 255), liste_texte = []) -> None:
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
        
        # Liste de texte
        self.liste_texte = liste_texte
        
        if self.liste_texte != []:
            self.texte = []
            for texte in self.liste_texte:
                self.texte.append(jeu.police.render(texte, True, couleur_texte))
        
        
    
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
        if len(self.liste_texte) > 1:
            for num, texte in enumerate(self.texte):
                fenetre.blit(texte, (self.x + (self.largeur / 2 - texte.get_width() / 2), self.y + (self.hauteur / 2 - texte.get_height() / 2) + (num * texte.get_height())))
        else:
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
                elif self.action == "Reprendre":
                    jeu.page.pause = not jeu.page.pause
                elif self.action == "Niv1":
                    jeu.page = JeuJoueur(33, 20, 3)
                    jeu.niveauPrec = "Niv1"
                elif self.action == "Niv2":
                    jeu.page = JeuJoueur(20, 60, 2)
                    jeu.niveauPrec = "Niv2"
                elif self.action == "Niv3":
                    jeu.page = JeuJoueur(10, 100, 1)
                    jeu.niveauPrec = "Niv3"
    
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
            self.x_origine = self.x
        
        if hauteurConteneur > 0:
            self.y = self.centrerHauteur(hauteurConteneur, yConteneur)
            self.y_origine = self.y
            
        self.rendu = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
        return self




class Page:
    def __init__(self) -> None:
        pass
    
    def afficher(self):
        jeu.fenetre.blit(self.image, (0, 0))
        for bouton in self.boutons:
            bouton.afficher(jeu.fenetre)
        
        if isinstance(self, JeuJoueur):
            if self.balles == [] and self.vies == 0:
                jeu.page = FinPartie("Vous avez perdu !", (255, 0, 0))
            elif self.nbBriques == 0:
                jeu.page = FinPartie("Vous avez gagné !", (0, 255, 0))
            else:
                if not self.pause:
                    self.actualiser()
                    
                self.raquette.afficher()
                for balle in self.balles:
                    balle.afficher()

                for ligne in self.briques.elements:
                    for brique in ligne.elements:
                        brique.afficher()

                for bonus in self.bonus:
                    bonus.afficher()

                for texte in self.textes.elements:
                    texte.afficher()
                
                if self.temps_affichage_texte is not None and pygame.time.get_ticks() < self.temps_affichage_texte + 3000:
                    for texte in self.texte_affichage_bonus.elements:
                        texte.afficher()
                    
                elif self.temps_affichage_texte is not None and pygame.time.get_ticks() >= self.temps_affichage_texte + 3000:
                    self.temps_affichage_texte = None
                if self.pause:
                    self.pauseP.afficher()
        if isinstance(self, FinPartie):
            self.texte.elements[0].afficher()

class FinPartie(Page):
    def __init__(self, texte, couleur) -> None:
        self.image = jeu.imageJeu
        self.texte = Texte(texte, couleur, 0, 0, 100, 50, 60)
        self.texte = Flexbox([self.texte], 1, 0.10, flex_direction = "row", justify_content = "space-between", y = 0.25)
        
        self.boutonRecommencer = Boutons(jeu.fenetre, "Recommencer", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255), arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10, arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35, action = jeu.niveauPrec)
        self.boutonAccueil = Boutons(jeu.fenetre, "Accueil", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255), arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10, arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35, page = Accueil)
        self.boutonQuitter = Boutons(jeu.fenetre, "Quitter", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255), arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10, arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35, action = "Quitter")
        
        self.boutons = [self.boutonRecommencer, self.boutonAccueil, self.boutonQuitter]
        self.interfaceB = Flexbox(self.boutons, 0.90, 0.275, flex_direction="row", justify_content="space-between", taux_espace_justify=0.1, centrer_largeur=True, y = 0.60)

class Accueil(Page):
    def __init__(self) -> None:
        # Chargement de l'image de fond
        self.image = jeu.imageMenu
        
        self.boutonJouer = Boutons(jeu.fenetre, "Jouer", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255),
                                           arrondissement_haut_gauche=10, arrondissement_haut_droit=10,
                                           arrondissement_bas_gauche=35, arrondissement_bas_droit=35,
                                           page = Niveaux)
        
        self.boutonOptions = Boutons(jeu.fenetre, "Options", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255),
                                     arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10,
                                     arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35)

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
        
        self.boutonBoutique = Boutons(jeu.fenetre, "Boutique", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255),
                                arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10,
                                arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35)
        
        self.boutonCompte = Boutons(jeu.fenetre, "Compte", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255),
                                    arrondissement_haut_gauche=10, arrondissement_haut_droit=10,
                                    arrondissement_bas_gauche=35, arrondissement_bas_droit=35)
        
        self.boutonJPersonnalisation = Boutons(jeu.fenetre, "Personnalisation", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255),
                                           arrondissement_haut_gauche=10, arrondissement_haut_droit=10,
                                           arrondissement_bas_gauche=35, arrondissement_bas_droit=35)
        
        
        self.boutons1 = [self.boutonJouer, self.boutonOptions, self.boutonAide, self.boutonScores, self.boutonQuitter]
        self.boutons2 = [self.boutonCompte, self.boutonJPersonnalisation]
        self.boutons3 = [self.boutonBoutique]
        
        self.boutons = self.boutons1 + self.boutons2 + self.boutons3
        
        menu = Flexbox(self.boutons1, 0.20, 0.45, flex_direction="column", align_content="space-between", taux_espace_align=0.1, centrer_largeur=True, y = 0.45)
        menu2 = Flexbox(self.boutons2, 0.20, 0.45, flex_direction="column", align_content="space-between", taux_espace_align=0.1, centrer_largeur=True, y = 0.45)
        menu3 = Flexbox(self.boutons3, 0.20, 0.45, flex_direction="column", align_content="space-between", taux_espace_align=0.1, centrer_largeur=True, y = 0.45)
        liste_menu = [menu2, menu, menu3]
        menu4 = Flexbox(liste_menu, 0.90, 0.45, flex_direction="row", justify_content="space-between", taux_espace_justify=0.1, centrer_largeur=True, y = 0.45)
        
class Niveaux(Page):
    def __init__(self) -> None:
        # Chargement de l'image de fond
        self.image = jeu.imageMenu
        
        self.boutonAccueil = Boutons(jeu.fenetre, "Accueil", 20, 20, 200, 100, (30, 30, 30), (255, 255, 255), arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10, arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35, page = Accueil)
        self.boutonNiveau1 = Boutons(jeu.fenetre, "Niveau 1", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255), arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10, arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35, action = "Niv1")
        self.boutonNiveau2 = Boutons(jeu.fenetre, "Niveau 2", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255), arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10, arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35, action = "Niv2")
        self.boutonNiveau3 = Boutons(jeu.fenetre, "Niveau 3", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255), arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10, arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35, action = "Niv3")
        self.boutonNiveauIA = Boutons(jeu.fenetre, "Niveau IA", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255), arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10, arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35, page = Accueil)
        
        self.boutons = [self.boutonAccueil, self.boutonNiveau1, self.boutonNiveau2, self.boutonNiveau3, self.boutonNiveauIA]
        self.boutonsInterface = [self.boutonNiveau1, self.boutonNiveau2, self.boutonNiveau3, self.boutonNiveauIA]
        interface = Flexbox(self.boutonsInterface, 0.90, 0.45, flex_direction="row", justify_content="space-between", taux_espace_justify=0.1, centrer_largeur=True, y = 0.45)

class JeuJoueur(Page):
    def __init__(self, taux_bonus, taux_renforcee, vies) -> None:
        # Changement de l'image de fond
        self.image = jeu.imageJeu
        
        # Raquette
        self.raquette = Raquette()
        
        # Balle
        self.balles = []
        for i in range(1):
            self.balles.append(Balle())

        # Bonus
        self.bonus = []
        self.temps_affichage_texte = None
        self.texte_affichage_bonus_temp = []
        self.texte_affichage_bonus = None

        # Briques
        self.briques = []
        for i in range(15):
            liste_temp = []
            for j in range(7):
                liste_temp.append(Brique(taux_renforcee, taux_bonus, 100, 100, 100, 50, (255, 255, 255)))
            liste_temp = Flexbox(liste_temp, 1, 1, flex_direction = "column", align_content = "space-between", taux_espace_align = 0.1)
            self.briques.append(liste_temp)
        self.briques = Flexbox(self.briques, 0.98, 0.30, flex_direction = "row", justify_content = "space-between", taux_espace_justify = 0.1, centrer_largeur=True, y = 0.01)
        self.nbBriques = len(self.briques.elements) * len(self.briques.elements[0].elements)
        
        # Autres
        self.vies = vies
        self.pause = False
        self.pauseP = Pause()
        self.boutons = []
        
        # Textes
        self.texteScore = Texte("Score : 0", (0, 0, 0), 0, 0, 100, 50)
        self.texteVies = Texte("Vies : " + str(self.vies), (0, 0, 0), 0, 0, 100, 50)
        self.textenbBriques = Texte("Briques : " + str(self.nbBriques), (0, 0, 0), 0, 0, 100, 50)
        
        self.textes = [self.texteScore, self.texteVies, self.textenbBriques]
        self.textes = Flexbox(self.textes, 1, 0.10, flex_direction = "row", justify_content = "space-between", taux_espace_justify = 0.1, centrer_largeur=True, y = 0.90)
    
    def actualiser_textes(self):
        self.texteScore = Texte("Score : 0", (0, 0, 0), 0, 0, 100, 50)
        self.texteVies = Texte("Vies : " + str(self.vies), (0, 0, 0), 0, 0, 100, 50)
        self.textenbBriques = Texte("Briques : " + str(self.nbBriques), (0, 0, 0), 0, 0, 100, 50)
        self.textes = [self.texteScore, self.texteVies, self.textenbBriques]
        self.textes = Flexbox(self.textes, 1, 0.10, flex_direction = "row", justify_content = "space-between", taux_espace_justify = 0.1, centrer_largeur=True, y = 0.90)
    
    def actualiser(self):
        for balle in self.balles:
            balle.actualiser()
        self.raquette.actualiser()
        for bonus in self.bonus:
            bonus.actualiser()
        self.actualiser_textes()

class Pause(Page):
    def __init__(self):
        self.couleur_transparente_opaque = (0, 0, 0, 128)  # 128 pour une opacité partielle
        # Création d'une surface transparente avec une opacité partielle
        self.image = pygame.Surface((jeu.largeur, jeu.hauteur), pygame.SRCALPHA)
        self.image.fill(self.couleur_transparente_opaque)
        
        self.boutonReprendre = Boutons(jeu.fenetre, "Reprendre", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255), arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10, arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35, action = "Reprendre")
        self.boutonOptions = Boutons(jeu.fenetre, "Options", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255),arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10, arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35)
        self.boutonAccueil = Boutons(jeu.fenetre, "Accueil", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255), arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10, arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35, page = Accueil)
        self.boutonQuitter = Boutons(jeu.fenetre, "Quitter", 100, 100, 350, 80, (30, 30, 30), (255, 255, 255), arrondissement_haut_gauche = 10, arrondissement_haut_droit = 10, arrondissement_bas_gauche = 35, arrondissement_bas_droit = 35, action = "Quitter")

        self.boutons = [self.boutonReprendre, self.boutonOptions, self.boutonAccueil, self.boutonQuitter]
        jeu.page.boutons = self.boutons
        self.interface = Flexbox(self.boutons, 0.20, 0.40, flex_direction="column", align_content="space-between", taux_espace_align=0.1, centrer_largeur = True, centrer_hauteur = True)

class Brique:
    def __init__(self, taux_renforcee, taux_bonus, x = 0, y = 0, largeur = 0, hauteur = 0, couleur = (255, 255, 255)) -> None:
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur

        renforcee = random.randint(0, 100)
        bonus = random.randint(0, 100)
        bonusC = ["Vie", "Taille", "X2", "X4", "X7", "X10"]
        bonusC_poids = [0.25, 0.20, 0.25, 0.15, 0.08, 0.07]
        if bonus <= taux_bonus:
            self.bonus = random.choices(bonusC, bonusC_poids)[0]
            self.couleur = (0, 255, 0)
        else:
            self.bonus = None
        
        if renforcee <= taux_renforcee:
            self.vies = 2
            if self.bonus == None:
                self.couleur = (255, 0, 0)
            else:
                self.couleur = (255, 255, 0)
        else:
            self.vies = 1
        self.rendu = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
    
    
    def afficher(self):
        pygame.draw.rect(jeu.fenetre, self.couleur, self.rendu)

class Raquette:
    def __init__(self):
        # Dimensions
        self.largeur = (jeu.largeur / 100) * 10
        self.hauteur = (jeu.hauteur / 100) * 2
        
        # Coordonnées
        self.x = jeu.largeur / 2 - self.largeur / 2
        self.y = jeu.hauteur - self.hauteur - ((jeu.hauteur / 100) * 10)
        
        # Autres
        self.rendu = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
        self.couleur = (255, 255, 255)
        self.vitesse = (jeu.largeur / 100) * 0.075
        self.gauche = False
        self.droite = False
    
    def actualiser(self):
        # Déplacement de la raquette
        if self.gauche:
            self.x -= self.vitesse * jeu.dt
        if self.droite:
            self.x += self.vitesse * jeu.dt
        
        # Vérifier que la raquette ne sorte pas de l'écran
        if self.x < 0:
            self.x = 0
        if self.x + self.largeur > jeu.largeur:
            self.x = jeu.largeur - self.largeur
        
        # Actualiser le rendu de la raquette
        self.rendu = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)

    def afficher(self):
        pygame.draw.rect(jeu.fenetre, self.couleur, self.rendu)

class Balle:
    def __init__(self, x = 0, y = 0, diametre = 0):
        # Dimensions
        if diametre != 0:
            self.diametre = diametre
        else:
            self.diametre = (jeu.largeur / 100) * 1.5
        
        # Position
        if x != 0 and y != 0:
            self.position = pygame.Vector2(x, y)
        else:
            self.position = pygame.Vector2(jeu.largeur / 2, jeu.hauteur / 2)
        
        # Vitesse et direction
        angle = random.randint(200, 340)
        self.vitesse = pygame.Vector2(math.cos(math.radians(angle)), math.sin(math.radians(angle))) * (jeu.largeur / 100) * 0.05
        
        # Autres
        self.couleur = (0, 0, 0)
    
    def collisions_murs(self):
        if self.position.x - self.diametre / 2 < 0:
            self.vitesse.x *= -1
            self.position.x = self.diametre / 2
        elif self.position.x + self.diametre / 2 > jeu.largeur:
            self.vitesse.x *= -1
            self.position.x = jeu.largeur - self.diametre / 2
        if self.position.y - self.diametre / 2 < 0:
            self.vitesse.y *= -1
            self.position.y = self.diametre / 2
        elif self.position.y > jeu.hauteur:
            jeu.page.balles.remove(self)
    
    def collisions_raquette(self):
        rayon = self.diametre / 2
        rect_balle = pygame.Rect(self.position.x - rayon, self.position.y - rayon, self.diametre, self.diametre)
        if rect_balle.colliderect(jeu.page.raquette.rendu):
            self.vitesse.y *= -1
            self.position.y = jeu.page.raquette.y - rayon - 1
            if jeu.page.raquette.gauche:
                self.vitesse = self.vitesse.rotate(-20)  # Modifier cette valeur pour ajuster l'effet
            if jeu.page.raquette.droite:
                self.vitesse = self.vitesse.rotate(20)  # Modifier cette valeur pour ajuster l'effet

    def collisions_briques(self):
        rayon = self.diametre / 2
        for ligne in jeu.page.briques.elements:
            for brique in ligne.elements:
                if brique.rendu.collidepoint(self.position.x, self.position.y - rayon):
                    self.mise_a_jour_brique(ligne, brique)
                    self.vitesse.y *= -1
                    break
                elif brique.rendu.collidepoint(self.position.x, self.position.y + rayon):
                    self.mise_a_jour_brique(ligne, brique)
                    self.vitesse.y *= -1
                    break
                elif brique.rendu.collidepoint(self.position.x - rayon, self.position.y):
                    self.mise_a_jour_brique(ligne, brique)
                    self.vitesse.x *= -1
                    break
                elif brique.rendu.collidepoint(self.position.x + rayon, self.position.y):
                    self.mise_a_jour_brique(ligne, brique)
                    self.vitesse.x *= -1
                    break
                
                elif brique.rendu.collidepoint(self.position.x + (rayon * -0.5), self.position.y + (rayon * (sqrt(3) / 2))):
                    self.mise_a_jour_brique(ligne, brique)
                    self.vitesse.y *= -1
                    break
                elif brique.rendu.collidepoint(self.position.x + (rayon * 0.5), self.position.y + (rayon * (sqrt(3) / 2))):
                    self.mise_a_jour_brique(ligne, brique)
                    self.vitesse.y *= -1
                    break
                elif brique.rendu.collidepoint(self.position.x + (rayon * -0.5), self.position.y + (rayon * (-sqrt(3) / 2))):
                    self.mise_a_jour_brique(ligne, brique)
                    self.vitesse.y *= -1
                    break
                elif brique.rendu.collidepoint(self.position.x + (rayon * 0.5), self.position.y + (rayon * (-sqrt(3) / 2))):
                    self.mise_a_jour_brique(ligne, brique)
                    self.vitesse.y *= -1
                    break
                
                elif brique.rendu.collidepoint(self.position.x + (rayon * (sqrt(3) / 2)), self.position.y + (rayon * -0.5)):
                    self.mise_a_jour_brique(ligne, brique)
                    self.vitesse.x *= -1
                    break
                elif brique.rendu.collidepoint(self.position.x + (rayon * (sqrt(3) / 2)), self.position.y + (rayon * 0.5)):
                    self.mise_a_jour_brique(ligne, brique)
                    self.vitesse.x *= -1
                    break
                elif brique.rendu.collidepoint(self.position.x + (rayon * (-sqrt(3) / 2)), self.position.y + (rayon * -0.5)):
                    self.mise_a_jour_brique(ligne, brique)
                    self.vitesse.x *= -1
                    break
                elif brique.rendu.collidepoint(self.position.x + (rayon * (-sqrt(3) / 2)), self.position.y + (rayon * 0.5)):
                    self.mise_a_jour_brique(ligne, brique)
                    self.vitesse.x *= -1
                    break
    
    def mise_a_jour_brique(self, ligne, brique):
        brique.vies -= 1
        if brique.vies == 0:
            ligne.elements.remove(brique)
            jeu.page.nbBriques -= 1
            if brique.bonus != None:
                jeu.page.bonus.append(Bonus(brique.x + (brique.largeur / 2), brique.y + (brique.hauteur / 2), brique.bonus))
        elif brique.vies == 1:
            if brique.bonus == None:
                brique.couleur = (255, 255, 255)
            else:
                brique.couleur = (0, 255, 0)
    
    def actualiser(self):
        self.position += self.vitesse * jeu.dt
        self.collisions_murs()
        self.collisions_raquette()
        self.collisions_briques()
    
    def afficher(self):
        pygame.draw.circle(jeu.fenetre, self.couleur, (int(self.position.x), int(self.position.y)), int(self.diametre / 2))

class Bonus:
    def __init__(self, x, y, type_bonus):
        self.x = x
        self.y = y
        self.diametre = (jeu.largeur / 100) * 2
        self.type_bonus = type_bonus
        self.couleur = (255, 0, 0)
        self.vitesse = (jeu.largeur / 100) * 0.02

    def collisions_raquette(self):
        rayon = self.diametre / 2
        rect_bonus = pygame.Rect(self.x - rayon, self.y - rayon, self.diametre, self.diametre)
        if rect_bonus.colliderect(jeu.page.raquette.rendu):
            if self.type_bonus == "Vie":
                jeu.page.vies += 1
            elif self.type_bonus == "Taille":
                jeu.page.raquette.largeur += (jeu.largeur / 100) * 2
            elif self.type_bonus == "X2":
                liste_temp = []
                for balle in jeu.page.balles:
                    liste_temp.append(Balle(balle.position.x, balle.position.y, balle.diametre))
                jeu.page.balles += liste_temp
            elif self.type_bonus == "X4":
                liste_temp = []
                for balle in jeu.page.balles:
                    for i in range(3):
                        liste_temp.append(Balle(balle.position.x, balle.position.y, balle.diametre))
                jeu.page.balles += liste_temp
            elif self.type_bonus == "X7":
                liste_temp = []
                for balle in jeu.page.balles:
                    for i in range(6):
                        liste_temp.append(Balle(balle.position.x, balle.position.y, balle.diametre))
                jeu.page.balles += liste_temp
            elif self.type_bonus == "X10":
                liste_temp = []
                for balle in jeu.page.balles:
                    for i in range(9):
                        liste_temp.append(Balle(balle.position.x, balle.position.y, balle.diametre))
                jeu.page.balles += liste_temp
            jeu.page.bonus.remove(self)
            jeu.page.temps_affichage_texte = pygame.time.get_ticks()
            jeu.page.texte_affichage_bonus_temp.append(Texte(self.type_bonus, (0, 0, 0), 0, 0, 100, 50, 30))
            jeu.page.texte_affichage_bonus = Flexbox(jeu.page.texte_affichage_bonus_temp, 0.20, 0.40, flex_direction="column", align_content="space-between", taux_espace_align=0.1, x = 0.80, y = 0.45)
    
    def actualiser(self):
        if self.y > jeu.hauteur:
            jeu.page.bonus.remove(self)
        self.collisions_raquette()
        self.y += self.vitesse * jeu.dt
    
    def afficher(self):
        pygame.draw.circle(jeu.fenetre, self.couleur, (int(self.x), int(self.y)), self.diametre / 2)

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
        
        # Fenêtre
        self.fps = 144
        self.largeur = 1920# 3840 | 2560
        self.hauteur = 1080# 2160 | 1440
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        
        self.horloge = pygame.time.Clock()
        
        # Chargement des images
        self.imageMenu = pygame.image.load("img/Menu.jpg").convert()
        self.imageMenu = pygame.transform.scale_by(self.imageMenu, (self.largeur / self.imageMenu.get_width()))
        
        self.imageJeu = pygame.image.load("img/fond_blanc.jpg").convert()
        self.imageJeu = pygame.transform.scale_by(self.imageJeu, (self.largeur / self.imageJeu.get_width()))
        
        # Police
        self.policeOrig = "font/PressStart2P-Regular.ttf"
        self.police = pygame.font.Font("font/PressStart2P-Regular.ttf", 27)
        
        self.executer = True
        self.niveauPrec = None
        
        self.position_souris = pygame.mouse.get_pos()
    
    def gerer_evenements(self):
        """Cette méthode permet de gérer les événements du jeu
        """
        
        
        # A revoir
        if isinstance(self.page, JeuJoueur):
            if self.page.pause:
                boutons = self.page.pauseP.boutons
            else:
                boutons = self.page.boutons
        else:
            boutons = self.page.boutons
        
        
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                self.executer = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                for bouton in boutons:
                    bouton.cliquer()
                    
            if isinstance(self.page, JeuJoueur):
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_LEFT:
                        self.page.raquette.gauche = True
                    if evenement.key == pygame.K_RIGHT:
                        self.page.raquette.droite = True
                    if evenement.key == pygame.K_ESCAPE:
                        self.page.pause = not self.page.pause
                    if evenement.key == pygame.K_SPACE:
                        if jeu.page.vies > 0:
                            self.page.balles.append(Balle())
                            jeu.page.vies -= 1
                
                if evenement.type == pygame.KEYUP:
                    if evenement.key == pygame.K_LEFT:
                        self.page.raquette.gauche = False
                    if evenement.key == pygame.K_RIGHT:
                        self.page.raquette.droite = False
        
        # Cette condition permet de savoir si la souris a bougé, et donc de ne pas faire des calculs inutiles
        position_souris_temp = pygame.mouse.get_pos()
        if position_souris_temp != self.position_souris:
            self.position_souris = position_souris_temp
            # Si le bouton est survolé, il change de couleur et s'enfonce
            for bouton in boutons:
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
            self.dt = self.horloge.tick(self.fps)
            self.fenetre.fill((255, 255, 255))
            self.page.afficher()
            self.fenetre.blit(self.police.render(str(round(self.horloge.get_fps(), 2)), True, (255, 255, 255)), (0, 0))
            self.gerer_evenements()
            pygame.display.flip()


jeu = Jeu()
jeu.executer_jeu()