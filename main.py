import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True == True:
    log_state()

    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
		return

    screen.fill('black')
    pygame.display.flip

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
