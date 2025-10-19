import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #get a new GUI window
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    dt =0
    #Create 2 groups updatable and drawable
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = updatable, drawable #assign the groups to the Player class so that any new Player object is added to these groups automatically
    while True:
        # make the window exit button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color="black")
        # Change the game loop to use the new groups instead of the Player object directly.
        drawable.draw(screen) # prev: player.draw(screen) 
        updatable.update(dt)  # prev: player.update(dt) - as objeccts increases, it gets more cluttered, so we use groups
        pygame.display.flip() # refresh the screen
        dt = clock.tick(60) /1000 # delta time in seconds
         
        

if __name__ == "__main__":
    main()
