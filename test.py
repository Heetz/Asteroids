import pygame
import sys
import os

print(f"DISPLAY={os.environ.get('DISPLAY')}")
print(f"SDL_VIDEODRIVER={os.environ.get('SDL_VIDEODRIVER')}")

try:
    print("Starting pygame test...")
    pygame.init()
    print("Pygame initialized")

    screen = pygame.display.set_mode((300, 300))
    print("Display set")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255, 0, 0))
        pygame.display.flip()
        print("Screen updated")
        pygame.time.delay(1000)  # 1 second delay

except Exception as e:
    print(f"Error occurred: {e}")
finally:
    pygame.quit()
    print("Pygame closed")