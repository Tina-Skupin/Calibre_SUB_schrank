print ("Hello World semicolon")
#test: if it prints, skript executes


import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1800, 900))
clock = pygame.time.Clock()
running = True

#creating the shelf
Rect = pygame.Rect
shelf1 = Rect(100, 700, 1600, 50)

#creating the books
book = Rect(100, 200, 70, 500)
book2 = Rect(170, 250, 80, 450)
book3 = Rect(250, 200, 60, 500)
book4 = Rect(310, 200, 70, 500)
book5 = Rect(380, 630, 500, 70)


#creating the text
titles = ['Valkyrie- Zurück ins jetzt', 'Valkyrie- Ruf des Schicksals', 'Valkyrie- Hels Armee','Valkyrie- Stockholm brennt','Valkyrie- Ragnarök']
screentexts = []
for title in titles:
    font = pygame.font.SysFont(None, size=40)
    titletext = font.render(title, True, (255, 155, 0))
    screentext = pygame.transform.rotate(titletext, 90)
    screentexts.append(screentext)


#text creation, old
#creating the text
# Choose a font
font = pygame.font.SysFont('Arial', 40)
# Render the text
text = font.render('Valkyrie- Zurück ins jetzt', True, (255, 155, 0))
# Rotate the text
valkyrie1 = pygame.transform.rotate(text, 90)

text2 = font.render('Valkyrie- Ruf des Schicksals', True, (0, 155, 0))
valkyrie2 = pygame.transform.rotate(text2, 90)

text3 = font.render('Valkyrie- Hels Armee', True, (255, 155, 0))
valkyrie3 = pygame.transform.rotate(text3, 90)

text4 = font.render('Valkyrie- Stockholm brennt', True, (255, 155, 0))
valkyrie4 = pygame.transform.rotate(text4, 90)


valkyrie5 = font.render('Valkyrie- Ragnarök', True, (255, 155, 0))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")

    pygame.draw.rect(screen, (200, 166, 45), shelf1)
    pygame.draw.rect(screen, (0, 255, 16), book)
    pygame.draw.rect(screen, (207, 166, 16), book2)
    pygame.draw.rect(screen, (0, 100, 16), book3)
    pygame.draw.rect(screen, (0, 255, 16), book4)
    pygame.draw.rect(screen, (0, 100, 16), book5)

    # Display the text
    Band1 = valkyrie1.get_rect(center=(130, 500))
    screen.blit(valkyrie1, Band1)

    Band2 = valkyrie2.get_rect(center=(205, 500))
    screen.blit(valkyrie2, Band2)   

    Band3 = valkyrie3.get_rect(center=(285, 500))
    screen.blit(valkyrie3, Band3)

    Band4 = valkyrie4.get_rect(center=(350, 500))
    screen.blit(valkyrie4, Band4)

    Band5 = valkyrie5.get_rect(center=(540, 680))
    screen.blit(valkyrie5, Band5)

    for wordsblubb in screentexts:
        blubb = wordsblubb.get_rect(center=(600, 680))
        screen.blit(wordsblubb, blubb)





    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()