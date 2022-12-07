https://eyewiki.aao.org/w/images/1/e/e3/17768_lores.jpg

# ACS1111: Herd Immunity Simulation
Python OOP Program

## Description
Python program which utilizes OOP to model how a virus moves through a population where some (but not all) of a population is vaccinated against a virus.

## Rules of the Simulation
1. A sick person only has a chance at infecting uninfected, unvaccinated people they encounter.
2. An infected person cannot infect a vaccinated person. This still counts as an interaction.
3. An infected person cannot infect someone that is already infected. This still counts as an interaction.
4. At the end of a time step, an infected person will either die of the infection or get better. The chance they will die is the percentage chance stored in `mortality_rate`.
5. For simplicity's sake, if the person does not die, we will consider them immune to the virus and change `is_vaccinated` to `True` when this happens.
6. Dead people can no longer be infected, either. Any time an individual dies, we should also change their `infected` attribute to `False`.
7. All state changes for a person should occur at the **end** of a time step, after all infected persons have finished all of their interactions.
8. During the interactions, make note of any new individuals infected on this step. After the interactions are over, we will change the `infected` attribute of all newly infected individuals to `True`.
9. Resolve the states of all individuals that started the turn infected by determining if they die or survive the infection, and change the appropriate attributes.
10. The simulation should output a logfile that contains a record of every interaction that occurred during the simulation. We will use this logfile to determine final statistics and answer questions about the simulation.


## Usage
The program is designed to be run from the command line. You can do this by running

python3 simulation.py

followed by the command line arguments in the following order, separated by spaces: 

{population size} {vacc_percentage} {virus_name} {mortality_rate} {repro_rate} {optional: number of people initially infected (default is 1)}

Let's look at an example:

Population Size: 100,000
Vaccination Percentage: 90%
Virus Name: Ebola
Mortality Rate: 70%
Reproduction Rate: 25%
People Initially Infected: 10

In the terminal you would type the following to run the simulation:

python3 simulation.py 100000 0.90 Ebola 0.70 0.25 10



python3 simulation.py 100000 0.90 Ebola 0.70 0.25 10
