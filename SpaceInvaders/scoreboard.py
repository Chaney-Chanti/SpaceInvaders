import pygame as pg 
from os.path import exists

class Scoreboard:
    def __init__(self, game): 
        self.score = 0
        self.level = 0
        self.high_score = 0
        
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = (30, 30, 30)
        self.font = pg.font.SysFont(None, 48)

        self.score_image = None 
        self.score_rect = None
        self.prep_score()

    def increment_score(self): 
        self.score += self.settings.alien_points
        self.prep_score()

    def prep_score(self): 
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def save_score(self):
        f_exists = exists('highscore.txt')
        if f_exists:
            with open('highscore.txt', 'r') as f:
                highscore = f.readline()
            if self.score > int(highscore):
                with open('highscore.txt', 'w+') as f:
                    f.write(str(self.score))
        else:
            with open('highscore.txt', 'w') as f:
                f.write(str(self.score))

    def get_highscore(self):
        f_exists = exists('highscore.txt')
        if f_exists:
            with open('highscore.txt', 'w') as f:
                highscore = f.readline()
            return highscore
        return 0


    def reset(self): 
        self.score = 0
        self.update()

    def update(self): 
        # TODO: other stuff
        self.draw()

    def draw(self): 
        self.screen.blit(self.score_image, self.score_rect)