class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate 
        self.mortality_rate = mortality_rate


# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    print(virus.name)
    print(virus.repro_rate) 
    print(virus.mortality_rate)

    # Two Additional Tests
    ebola = Virus("Ebola", 1.51, 0.5 )
    assert ebola.name == "Ebola"
    assert ebola.repro_rate == 1.51
    assert ebola.mortality_rate == 0.5

    print("-------------------------")
    print(ebola.name)
    print(ebola.repro_rate) 
    print(ebola.mortality_rate)

    smallpox = Virus("Smallpox", 6.87, 0.8 )
    assert smallpox.name == "Smallpox"
    assert smallpox.repro_rate == 6.87
    assert smallpox.mortality_rate == 0.8

    print("-------------------------")
    print(smallpox.name)
    print(smallpox.repro_rate) 
    print(smallpox.mortality_rate)
