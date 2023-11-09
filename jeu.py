import pygame


class Bouton:
    def __init__(self, largeur, hauteur, couleur, texte, font, x, y):
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.texte = texte
        self.font = font
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, self.couleur, (self.x, self.y, self.largeur, self.hauteur), 0, 20)
        text = self.font.render(self.texte, True, "black")
        text_rect = text.get_rect(center = ((self.largeur /2) + self.x , (self.hauteur/2) + self.y))
        screen.blit(text, text_rect)

    def isClicked(self, x, y):
        if x > self.x and x < self.x + self.largeur and y > self.y and y < self.y + self.hauteur:
            print("clicked")
            return True
        else:
            return False




class Accueil:
    def __init__(self):
        self.font = pygame.font.SysFont("consolas", 20)

    def draw(self, screen):
        largeurEcran = jeu.largeur
        hauteurEcran = jeu.hauteur
        screen.fill("white")
        screen.blit(self.font.render("Accueil", True, "black", "purple"), (0, 0))
        Bouton(200, 50, (125, 160, 202), "Jouer", self.font, largeurEcran / 2 - 100, hauteurEcran / 2 - 25).draw(screen)



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
        self.acceuil = True
        
    def run(self):
        while self.running:
            # ==================== Event detection ====================
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            # ==================== Update ====================
            self.screen.fill("white")
            self.FramePerSec.tick(60) # 60 FPS limit
            if self.acceuil:
                Accueil().draw(self.screen)
            pygame.display.flip()

jeu = Jeu()
jeu.run()