import config
import player
import math
import species
import operator

class Population:
    def __init__(self, size):
        self.players = []
        self.generation = 1
        self.species = []
        self.size = size

        for i in range(0, self.size):
            self.players.append(player.Player())

    def update_live_players(self):
        for p in self.players:
            if p.alive:
                p.look()
                p.think()
                p.draw(config.window)
                p.update(config.ground)

    def natural_selection(self):
        print('SPECTIATE')
        self.speciate()

        print('CALCULATE FITNES')
        self.calculate_fitness()

        print('SORT BY FITNESS')
        self.sort_species_by_fitness()

        print('CHILDREN FOR NEXT GEN')
        self.next_gen()
    
    def speciate(self):
        for s in self.species:
            s.players = []

        for p in self.players:
            add_to_species = False
            for s in self.species:
                if s.similarity(p.brain):
                    s.add_to_species(p)
                    add_to_species = True
                    break
            if not add_to_species:
                self.species.append(species.Species(p))
    
    def calculate_fitness(self):
        for p in self.players:
            p.calculate_fitness()
        for s in self.species:
            s.calculate_average_fitness()
    
    def sort_species_by_fitness(self):
        for s in self.species:
            s.sort_species_by_fitness()
        
        self.species.sort(key = operator.attrgetter('benchmark_fitness'), reverse=True)
    
    def next_gen(self):
        children = []

        # Clone of champion is added to each species
        for s in self.species:
            children.append(s.champion.clone())
        
        # Fill open player slots
        children_per_species = math.floor((self.size - len(self.species)) / len(self.species))

        for s in self.species:
            for i in range(0, children_per_species):
                children.append(s.offspring())
        
        while len(children) < self.size:
            children.append(self.species[0].offspring())

        self.players = []
        for child in children:
            self.players.append(child)
        self.generation += 1
    
    # Return true if all players are dead
    def purge(self):
        purge = True
        for p in self.players:
            if p.alive:
                purge = False
        return purge

