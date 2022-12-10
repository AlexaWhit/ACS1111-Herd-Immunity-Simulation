import random
# random.seed(42)
from virus import Virus


class Person(object):
    # Define a person.
    def __init__(self, _id, is_vaccinated, infection = None):
        '''
        Initializes Person instance attributes:
        Id: Number
        is_vaccinated: Boolean
        infection: infection object
        '''

        self._id = _id  # int
        self.is_vaccinated = is_vaccinated # boolean
        self.infection = infection # infection object
        self.is_alive = True

    def did_survive_infection(self):
        '''
        This method checks if a person survived an infection and 
        updates is_alive, and is_vaccinated accordingly
        '''

        if self.infection:
            random_mortality = random.randint(0.0, 1.0)
            if random_mortality < self.infection.mortality_rate:
                print(f"{self._id} has died.")
                self.is_alive = False
            else:
                self.is_vaccinated = True
                self.infection = None
                self.is_alive = True
        return self.is_alive


        

if __name__ == "__main__":

    # Define a vaccinated person and check their attributes
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None
    print(vaccinated_person._id)
    print(vaccinated_person.is_alive)
    print(vaccinated_person.is_vaccinated)
    print(vaccinated_person.infection)

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None
    print(unvaccinated_person._id)
    print(unvaccinated_person.is_alive)
    print(unvaccinated_person.is_vaccinated)
    print(unvaccinated_person.infection)
    
    # Create a Virus object to give a Person object an infection
    virus = Virus("Ebola", 1.51, 0.5)

    # Create a Person object and give them the virus infection
    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is virus
    print(infected_person._id) 
    print(infected_person.is_alive)
    print(infected_person.is_vaccinated )
    print(infected_person.infection.name)
   
    # Create a list to hold 100 people. 
    people = []
    for i in range(1, 101):
        vaccinated = random.choice([True, False])
        new_person = Person(i, False, virus)
        people.append(new_person)

    # Now that you have a list of 100 people. Resolve whether the Person 
    # survives the infection or not by looping over the people list. Count
    # the people who survived and those who did not. 
    did_survive = 0
    did_not_survive = 0

    for person in people:
        survived = person.did_survive_infection()    
        if survived == True:
            did_survive +1;
        else:
            did_not_survive +1;
            
    print("Number of survivors:", did_survive)
    print("Number of deceased:", did_not_survive)

    # The results should roughly match the mortality rate of the virus
    # For example if the mortality rate is 0.2 rough 20% of the people 
    # should succumb. 

    # Stretch challenge! 
    # Check the infection rate of the virus by making a group of 
    # unifected people. Loop over all of your people. 
    # Generate a random number. If that number is less than the 
    # infection rate of the virus that person is now infected. 
    # Assign the virus to that person's infection attribute. 

    # Now count the infected and uninfect people from this group of people. 
    # The number of infectedf people should be roughly the same as the 
    # infection rate of the virus.