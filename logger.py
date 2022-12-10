class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        '''
        This method logs the initial starting metadata (including population, initial infected,
        the virus, and the initial vaccinated.
        '''
        file = open(self.file_name, "w")
        file.write(f"\t Virus: {virus_name}\n\t\tReproductive Rate: {basic_repro_num}%\n\t\tInitial Population Size: {pop_size}\n\t\tMortality Rate: {mortality_rate}%\n\t\tVaccination Rate: {vacc_percentage}%\n")
        file.close()

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        '''
        This method logs the steps, number of interactions, and the number of new infections.
        '''
        file = open(self.file_name, "a")
        file.write(f"\t Step Number: {step_number}\n\t Number of Interactions: {number_of_interactions}\n\t Number of New Infections: {number_of_new_infections}\n")
        file.close()

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        '''
        This method logs if the person survived, the currentl population count, and the number of new fatalities at each step.
        '''
        file = open(self.file_name, "a")
        file.write(f"\t Step Number: {step_number}\n\t Current Population: {population_count}\n\t Number of New Deaths: {number_of_new_fatalities}\n")
        file.close()

    def log_time_step(self, time_step_number):
        '''
        This method creates a line separation for each step.
        '''
        file = open(self.file_name, "a")
        file.write(f"\t Time Step Number: {time_step_number}")
        file.close()

    def log_final_summary(self, current_vaccinated, total_infected, total_dead, total_alive ):
        '''
        This method logs the final results of the simulation, to include the number of people vaccinated, the number of
        people alive and the number of dead. 
        '''
        file = open(self.file_name, "a")
        file.write(f"\t Total People Vaccinated: {current_vaccinated}\n\t Total People Infected: {total_infected}\n\t Total People Alive: {total_alive}\n\t Total People Dead: {total_dead}.")
        file.close()