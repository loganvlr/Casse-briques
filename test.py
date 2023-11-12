import pygame

pygame.init()

class Texte:
    """Classe permettant de créer un texte"""
    def __init__(self, texte, couleur, x = 0, y = 0):
        self.font = pygame.font.SysFont("consolas", 20)
        self.texte = texte
        self.couleur = couleur
        self.x = x
        self.y = y
        self.coor = (self.x, self.y)
        self.rendu = self.font.render(self.texte, True, self.couleur)

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
    def __init__(self, largeur, hauteur, couleur, x = 0, y = 0):
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.x = x
        self.y = y
        self.coor = (self.x, self.y)
        self.rendu = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)

    
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
            print("clicked")
            return True
        else:
            return False


screen = pygame.display.set_mode((1280, 720))
fps = 60
FramePerSec = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("white")
    
    boutonAccueil = Bouton(200, 50, (125, 160, 202)).centrer(1280, 720)
    pygame.draw.rect(screen, boutonAccueil.couleur, boutonAccueil.rendu, 0, 20)
    
    texteAcceuil = Texte("Accueil", "black").centrer(boutonAccueil.largeur, boutonAccueil.hauteur, boutonAccueil.x, boutonAccueil.y)
    screen.blit(texteAcceuil.rendu, texteAcceuil.coor)
    
    pygame.display.flip()
    FramePerSec.tick(fps)