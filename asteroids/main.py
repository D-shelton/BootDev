import pygame
from sys import exit
from constants import *
from player import *
from asteroid import *
from asteroidfield import *



def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 24)

    dt = 0
    score = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)
        for drw in drawable:
            drw.draw(screen)

        for ast in asteroids:
            if ast.check_col(player):
                print("Game over!")
                exit(0)
    
            for shot in shots:
                if shot.check_col(ast):
                    shot.kill()
                    ast.split()
                    score +=1

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(screen.get_width() * 0.95, screen.get_height() * 0.05))
        screen.blit(score_text, score_rect)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
