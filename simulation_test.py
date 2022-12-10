import pytest
from person import Person
from virus import Virus
from simulation import Simulation
from logger import Logger

# Test Simulation Class Below

if __name__ == "__main__":
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12

    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10
    virus = Virus(pop_size, vacc_percentage, initial_infected)
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)
    sim.run()