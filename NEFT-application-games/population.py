import config
import player

class Population:
    def __init__(self, size):
        self.players = []
        self.size = size

        for i in range(0, self.size):
            self.players.append(player.Player())

    def update_live_players(self):
        for p in self.players:
            if p.alive:
                p.think()
                p.draw(config.window)
                p.update(config.ground)
    
    # Return true if all players are dead
    def purge(self):
        purge = True
        for p in self.players:
            if p.alive:
                purge = False
        return purge

