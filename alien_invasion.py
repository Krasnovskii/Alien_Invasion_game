import sys
import pygame
from settings import Settings
from ship import Ship


class AlianInvesion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_hight))
        pygame.display.set_caption("Alian Invasion")

        self.ship = Ship(self)

    def run_game(self):

        # Start the main loop for the game
        while True:
            # Watch for keyboards and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass trhough the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitime()
            # Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # Make game instance and run
    ai = AlianInvesion()
    ai.run_game()
