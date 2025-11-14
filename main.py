import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #get a new GUI window
    clock = pygame.time.Clock()
    dt =0
    
    #Create 2 groups updatable and drawable
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable) #assign the groups to the Player class so that any new Player object is added to these groups automatically
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    #group all the asteroids in a separate group
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids) #assign the groups to the Asteroid class so that any new Asteroid object is added to these groups automatically

    #asteroid field
    AsteroidField.containers = updatable #asteroid field only needs to be updated, not drawn
    asteroid_field = AsteroidField()

    #shot group
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots) #assign the groups to the Shot class so that any new Shot object is added to these groups automatically

    while True:
        # make the window exit button work
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)  # prev: player.update(dt) - as objeccts increases, it gets more cluttered, so we use groups

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {Asteroid.score}", True, (255,255,255))
        screen.blit(score_text, (10, 10))

        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                print(f"Final Score: {Asteroid.score}")
                sys.exit()

            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill(color="black")
        # Change the game loop to use the new groups instead of the Player object directly.
        for obj in drawable:
            obj.draw(screen) # prev: player.draw(screen) 
        
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {Asteroid.score}", True, (255,255,255))
        screen.blit(score_text, (10, 10))


        pygame.display.flip() # refresh the screen
        dt = clock.tick(60) /1000 # delta time in seconds
         
        

if __name__ == "__main__":
    main()
