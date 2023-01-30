import pygame
import sys

pygame.init()
hintergrund = pygame.image.load("Grafiken/fluss.jpeg")
figur_links = pygame.image.load("Grafiken/surfer_links.png")
figur_rechts = pygame.image.load("Grafiken/surfer_rechts.png")
screen = pygame.display.set_mode([500,750])
clock = pygame.time.Clock()
pygame.display.set_caption("Ausweichen")

def zeichnen(list):
    screen.blit(hintergrund, (0, 0))
    #pygame.draw.rect(screen, (0, 255, 255), (x, y, breite, höhe))
    if list[0]:
        screen.blit(figur_links, (x,y))
    else:
        screen.blit(figur_rechts, (x,y))
    pygame.display.update()

x = 300
y = 600
breite = 100
höhe = 100
geschwindigkeit = 3

linkeWand = pygame.draw.rect(screen, (0,0,0), (1,0,2,750), 0)
rechteWand = pygame.draw.rect(screen, (0,0,0), (498,0,2,750), 0)


go = True
richtung = [0,0]
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    spielerRechteck = pygame.Rect(x,y,breite,höhe)
    gedrückt = pygame.key.get_pressed()

    #if gedrückt[pygame.K_UP]:
    #    y -= geschwindigkeit
    if gedrückt[pygame.K_RIGHT] and not spielerRechteck.colliderect(rechteWand):
        x += geschwindigkeit
        richtung = [0,1]
    #if gedrückt[pygame.K_DOWN]:
    #    y += geschwindigkeit
    if gedrückt[pygame.K_LEFT] and not spielerRechteck.colliderect(linkeWand):
        x -= geschwindigkeit
        richtung = [1,0]

    zeichnen(richtung)
    clock.tick(60)