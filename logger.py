class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    # You should log the results of each step. This should inlcude: 
    #   The population size, the number of living, the number of dead, and the number 
    #   of vaccinated people at that step. 
    # When the simulation concludes you should log the results of the simulation. 
    # This should include: 
    #   The population size, the number of living, the number of dead, the number 
    #   of vaccinated, and the number of steps to reach the end of the simulation. 

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        '''
        This method logs the initial starting metadata (including population, initial infected,
        the virus, and the initial vaccinated.
        '''

        file = open(self.file_name, "w")
        file.write('ACS1111 Herd Immunity Simulation\n')

        #Statistics
        file.write(f"Virus: {virus_name}\n\t\tReproductive Rate: {basic_repro_num}%\n\t\tInitial Population Size: {pop_size}\n\t\tMortality Rate: {mortality_rate}%\n\t\tVaccination Rate: {vacc_percentage}%\n")
        file.close()

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        '''
        This method logs the steps, number of interactions, and the number of new infections.
        '''
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        file = open(self.file_name, "a")
        file.write(f"Step Number: {step_number}********\n\t Number of Interactions: {number_of_interactions}\n\t Number of New Infections: {number_of_new_infections}\n")
        file.close()

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        '''
        This method logs the infection survival statistics to include
        '''
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        file = open(self.file_name, "w")

        file.close()

    def log_time_step(self, time_step_number):
        '''
        This method creates a line separation for each step.
        '''
        file = open(self.file_name, "w")

        file.close()

    def log_final_summary(self):
        '''
        This method logs the final results of the simulation, to include population size, the number of living, 
        the number of dead, the number of vaccinated, and the number of steps to reach the end of the simulation. 
        '''
        pass