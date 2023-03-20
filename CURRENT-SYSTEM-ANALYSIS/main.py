# importing the library
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

# main game loop
while running:
    # checks if the user clicks the X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white") # fills the screen with a color to wipe anyhting from last from

    ### GAME LOOP ###

    pygame.draw.circle(screen, "green", (300, 300), 40)
    pygame.draw.rect(screen, "grey", (100, 100, 200, 100))

    #################

    pygame.display.flip() # displays anything
    
    clock.tick(60) # sets fps to 60

pygame.quit()