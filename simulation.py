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
        # Create a Logger object and bind it to self.logger.
        self.logger = Logger('logger')
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.people = []
        self.population = self._create_population()
        self.newly_infected= []
        self.total_infected = []
        self.prevented_infection = []
        self.number_of_interactions = 0

        

    def _create_population(self):
        '''
        This method creates a population for the simulation. Some of the people will be infected and some
        will be uninfencted.
        '''

        people = []
        number_vaccinated = int((self.vacc_percentage/100) * self.pop_size)
        for i in range(1, int(self.pop_size)+1):
            if i<= self.initial_infected:
                person = Person(i, False, self.virus)
            elif number_vaccinated > 0:
                person = Person(i, True)
                number_vaccinated -=1
            else: 
                person = Person(i, False)
            people.append(person)
        return people


    def _simulation_should_continue(self):
        '''
        This method will return a boolean indicating if the simulation should continue. The simulation should not 
        continue if all of the people are dead, or if all of the living people have been vaccinated. 
        '''

        for person in self.people:
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
            

        # TODO: Write meta data to the logger. This should be starting 
        # statistics for the simulation. It should include the initial
        # population size and the virus. 
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 
        self.logger.log_completion_summary()


    def time_step(self, time_step_number):
        '''
        This method simulates interactions between people, calulates new infections, and determines if vaccinations 
        and fatalities from infections. The goal is have each infected person interact with a number of other 
         people in the population.
        '''

        interactions = 0
        for person in self.people:
            if person.infection != None and person.is_alive:
                for i in range(0, 100):
                    random_interaction = random.randint(0, self.pop_size-1)
                    self.interaction(person, self.people[random_interaction])
                    interactions += 1

        self.number_of_interactions += interactions
        

    def interaction(self, infected_person, random_person):
        '''
        This method simulates the interaction between a random person and an infected person. A random number is generated,
        and if that number is smaller than the reproduction rate, that person is now infected and is added to the 
        newly_infected array and their infected attribute is changed from False to True.
        '''

        if random_person.is_vaccinated == False and random.person.is_alive == True and random_person.infection == None:
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

        for person in self.people:
            if person in self.newly_infected:
                person.infection = self.virus
                self.infected_individuals += 1
        self.newly_infected = []



if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # Make a new instance of the imulation
    virus = Virus(virus, vacc_percentage, initial_infected)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    sim.run()
