print ("Hello World semicolon")

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1800, 920))
clock = pygame.time.Clock()
running = True

Rect = pygame.Rect
shelf1 = Rect(60, 600, 1600, 15)
book = Rect(100, 300, 70, 300)
book2 = Rect(170, 250, 80, 350)
book3 = Rect(250, 400, 60, 200)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.rect(screen, (207, 166, 45), shelf1)
    pygame.draw.rect(screen, (0, 255, 16), book)
    pygame.draw.rect(screen, (207, 166, 16), book2)
    pygame.draw.rect(screen, (0, 255, 16), book3)


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()