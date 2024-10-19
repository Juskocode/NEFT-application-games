import config
import player

class Population:
    def __init__(self):
        self.player = player.Player()

    def update_live_players(self):
        self.player.draw(config.window)