import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        '''
        Initializes Simulation instance attributes:
        virus: virus object
        pop_size: number
        vacc_percentage: number
        initial+infected: number
        '''
        
        self.logger = Logger("logger.txt")
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.population = self._create_population()
        self.newly_infected= []
        self.current_infected = 0
        self.total_infected = 0
        self.prevented_infection = 0
        self.newly_dead = 0
        self.current_deaths = []
        self.total_dead = 0
        self.number_of_interactions = 0
        self.current_vaccinated = 0
        self.total_alive = 0


        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)
      

    def _create_population(self):
        '''
        This method creates a population for the simulation. Some of the people will be infected and some
        will be uninfencted.
        '''

        population = []
        number_vaccinated = int((self.vacc_percentage/100) * self.pop_size)
        for i in range(1, int(self.pop_size)+1):
            if i<= self.initial_infected:
                person = Person(i, False, self.virus)
            elif number_vaccinated > 0:
                person = Person(i, True)
                number_vaccinated -=1
            else: 
                person = Person(i, False)
            population.append(person)
        return population


    def _simulation_should_continue(self):
        '''
        This method will return a boolean indicating if the simulation should continue. The simulation should not 
        continue if all of the people are dead, or if all of the living people have been vaccinated. 
        '''

        for person in self.population:
            if person.is_alive == True and person.is_vaccinated == False:
                return True
        return False


    def run(self):
        '''
        This method starts the simulation. It tracks the number of steps the simulation has run, checks if the 
        simulation should continue at the end of each step, and writes meta data to the logger which will be utilized
        as the starting statistics.
        '''

        time_step_counter = 0
        should_continue = True

        while should_continue:
            time_step_counter += 1
            self.time_step(time_step_counter)
            should_continue = self._simulation_should_continue()
            

        # Write meta data to the logger.
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

        #Send final data to logger
        total_vaccinated = 0
        for person in self.population:
            if person.is_alive == True:
                self.total_alive += 1
            elif person.is_alive == False:
                self.total_dead += 1
            elif person.is_vaccinated and person.is_alive:
                total_vaccinated += 1

        self.logger.log_completion_summary(self.total_alive, self.total_dead, self.total_infected, total_vaccinated)


    def time_step(self, time_step_number):
        '''
        This method simulates interactions between people, calulates new infections, and determines if vaccinations 
        and fatalities from infections. The goal is have each infected person interact with a number of other 
         people in the population.
        '''

        interactions = 0
        for person in self.population:
            if person.infection != None and person.is_alive:
                for i in range(0, 100):
                    random_interaction = random.randint(0, self.pop_size-1)
                    self.interaction(person, self.population[random_interaction])
                    interactions += 1

        self.number_of_interactions += interactions
        self.logger.log_time_step(time_step_number)
        self.logger.log_interactions(time_step_number, interactions, len(self.newly_infected))
        self._infect_newly_infected()

        # Determine vaccinations or fatalities from infections
        newly_dead = 0
        total_alive = 0
        for person in self.population:
            if person.infection != None and person.is_alive == True:
                if person.did_survive_infection()[0]
                if currently_alive == False:
                    newly_dead += 1
                    self.current_deaths.append(person)
                    self.total_dead += 1
            if person.is_alive:
                total_alive += 1

        self.logger.log_infection_survival(total_alive, newly_dead)
        

    def interaction(self, infected_person, random_person):
        '''
        This method simulates the interaction between a random person and an infected person. A random number is generated,
        and if that number is smaller than the reproduction rate, that person is now infected and is added to the 
        newly_infected array and their infected attribute is changed from False to True.
        '''

        if random_person.is_vaccinated == False and random_person.is_alive == True and random_person.infection == None:
            random_number = random.random()
            if random_number < self.virus.repro_rate:
                self.total_infected += 1
                if random_person not in self.newly_infected:
                    self.newly_infected.append(random_person)
        elif random_person.is_vaccinated == True and random_person.is_alive == True and random_person.infection == None:
            self.prevented_infection += 1


    def _infect_newly_infected(self):
        '''
        This method is called at the end of every time step and selected people are infected
        based on the interaction method above.
        '''

        for person in self.population:
            if person in self.newly_infected:
                person.infection = self.virus
                self.total_infected += 1
        self.newly_infected = []



