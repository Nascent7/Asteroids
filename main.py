import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

# clock variable assigned to the .Clock() object
    clock = pygame.time.Clock() 
    dt = 0
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
# updates player rotation from method in player.py, and is called before frame is rendered 
        player.update(dt)
# can set color using .fill("color") or .fill((R,G,B)) color tupe must be within it's own ()
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

# converts milisec. to sec. and limits framerate to 60 FPS
        dt = clock.tick(60) / 1000 

    

# not part of main function - "This line ensures the main() function is only called when this file is 
# run directly; it won't run if it's imported as a module. 
# It's considered the "pythonic" way to structure an executable program in Python. 
# Technically, the program will work fine by just calling main(), 
# but you might get an angry letter from Guido van Rossum if you don't."
if __name__ == "__main__": 
    main()