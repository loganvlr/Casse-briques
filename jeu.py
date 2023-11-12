import pygame

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
            "Scores": Scores
        }
        if self.nom == "Quitter":
            exit(0)
        return mapping.get(self.nom, None)
    
    

class Interactions:
    """Classe permettant de gérer les interactions"""
    def click(self, x, y):
        if isinstance(jeu.page, Accueil):                                       # match case aurait été plus propre mais pas dispo en python 3.8
            boutons = Accueil().boutonsAccueil
            
        elif isinstance(jeu.page, Niveaux):
            boutons = Niveaux().boutonsNiveaux
            
        elif isinstance(jeu.page, Options):
            boutons = Options().boutonsOptions
            
        elif isinstance(jeu.page, Aide):
            boutons = Aide().boutonsAide
            
        elif isinstance(jeu.page, Scores):
            boutons = Scores().boutonsScores
            
        else:
            boutons = []

        for bouton in boutons:
            if bouton.isClicked(x, y):
                print("clicked", bouton.nom)
                page_classe = bouton.get_page()
                print(page_classe)
                if page_classe is not None:
                    jeu.page = page_classe()
                    print(jeu.page)
                return True
        return False


# ==================== Pages ====================
class Accueil:

    boutonJouer = Bouton("Niveaux", 200, 50, (125, 160, 202)).centrer(1280, 720)
    texteJouer = Texte("Jouer", "white").centrer(boutonJouer.largeur, boutonJouer.hauteur, boutonJouer.x, boutonJouer.y)
    boutonOptions = Bouton("Options", 200, 50, (125, 160, 202)).centrer(1280, 720, 0, 60)
    texteOptions = Texte("Options", "white").centrer(boutonOptions.largeur, boutonOptions.hauteur, boutonOptions.x, boutonOptions.y)
    boutonQuitter = Bouton("Quitter", 200, 50, (125, 160, 202)).centrer(1280, 720, 0, 120)
    texteQuitter = Texte("Quitter", "white").centrer(boutonQuitter.largeur, boutonQuitter.hauteur, boutonQuitter.x, boutonQuitter.y)
    boutonAide = Bouton("Aide", 200, 50, (125, 160, 202)).centrer(1280, 720, 0, 180)
    texteAide = Texte("Aide", "white").centrer(boutonAide.largeur, boutonAide.hauteur, boutonAide.x, boutonAide.y)
    boutonScores = Bouton("Scores", 200, 50, (125, 160, 202)).centrer(1280, 720, 0, 240)
    texteScores = Texte("Scores", "white").centrer(boutonScores.largeur, boutonScores.hauteur, boutonScores.x, boutonScores.y)
    
    boutonsAccueil = [boutonJouer, boutonOptions, boutonQuitter, boutonAide, boutonScores]
    textesAccueil = [texteJouer, texteOptions, texteQuitter, texteAide, texteScores]
    
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
    boutonAccueil = Bouton("Accueil", 200, 50, (125, 160, 202)).centrer(1280, 720)
    texteAccueil = Texte("Accueil", "white").centrer(boutonAccueil.largeur, boutonAccueil.hauteur, boutonAccueil.x, boutonAccueil.y)
    boutonOptions = Bouton("Options", 200, 50, (125, 160, 202)).centrer(1280, 720, 0, 60)
    texteOptions = Texte("Options", "white").centrer(boutonOptions.largeur, boutonOptions.hauteur, boutonOptions.x, boutonOptions.y)
    boutonQuitter = Bouton("Quitter", 200, 50, (125, 160, 202)).centrer(1280, 720, 0, 120)
    texteQuitter = Texte("Quitter", "white").centrer(boutonQuitter.largeur, boutonQuitter.hauteur, boutonQuitter.x, boutonQuitter.y)
    boutonAide = Bouton("Aide", 200, 50, (125, 160, 202)).centrer(1280, 720, 0, 180)
    texteAide = Texte("Aide", "white").centrer(boutonAide.largeur, boutonAide.hauteur, boutonAide.x, boutonAide.y)
    boutonScores = Bouton("Scores", 200, 50, (125, 160, 202)).centrer(1280, 720, 0, 240)
    texteScores = Texte("Scores", "white").centrer(boutonScores.largeur, boutonScores.hauteur, boutonScores.x, boutonScores.y)
    
    boutonsNiveaux = [boutonAccueil, boutonOptions, boutonQuitter, boutonAide, boutonScores]
    textesNiveaux = [texteAccueil, texteOptions, texteQuitter, texteAide, texteScores]
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.boutonAccueil.couleur, self.boutonAccueil.rendu, 0, 20)
        screen.blit(self.texteAccueil.rendu, self.texteAccueil.coor)

        pygame.draw.rect(screen, self.boutonOptions.couleur, self.boutonOptions.rendu, 0, 20)
        screen.blit(self.texteOptions.rendu, self.texteOptions.coor)
        
        pygame.draw.rect(screen, self.boutonQuitter.couleur, self.boutonQuitter.rendu, 0, 20)
        screen.blit(self.texteQuitter.rendu, self.texteQuitter.coor)
        
        pygame.draw.rect(screen, self.boutonAide.couleur, self.boutonAide.rendu, 0, 20)
        screen.blit(self.texteAide.rendu, self.texteAide.coor)
        
        pygame.draw.rect(screen, self.boutonScores.couleur, self.boutonScores.rendu, 0, 20)
        screen.blit(self.texteScores.rendu, self.texteScores.coor)

class Options:
    pass

class Aide:
    pass

class Scores:
    pass



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
                    if Interactions().click(mouse_x, mouse_y):
                        self.acceuil = False
            pygame.display.flip()

jeu = Jeu()
jeu.run()