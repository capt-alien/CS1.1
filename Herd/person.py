import random
import virus

class Person(object):


    def __init__(self, _id, is_vaccinated, infection):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infection = infection


    def did_survive_infection(self, mortality_rate):
        if self.infection == True and self.is_vaccinated == False:
            chance_of_death = random.randint(0,100)
            if chance_of_death <= (mortality_rate * 100):
                self.is_alive = False
            else:
                self.is_vaccinated = True
                self.infection = False
        else:
            pass


# Testing
# hiv = virus.Virus("HIV", .1, .3)
# alex = Person(1,False,True)
# alex.infection = True
#
# alex.did_survive_infection(hiv.mortality_rate)
#
# print(alex.is_alive)
# print(alex.is_vaccinated)

    '''
    Person objects will populate the simulation.

    _____Attributes______:

    _id: Int.  A unique ID assigned to each person.

    is_vaccinated: Bool.  Determines whether the person object is vaccinated against
        the disease in the simulation.

    is_alive: Bool. All person objects begin alive (value set to true).  Changed
        to false if person object dies from an infection.

    infection:  None or Virus object.  Set to None for people that are not infected.
        If a person is infected, will instead be set to the virus object the person
        is infected with.

    _____Methods_____:

    __init__(self, _id, is_vaccinated, infection=None):
        - self.alive should be automatically set to true during instantiation.
        - all other attributes for self should be set to their corresponding parameter
            passed during instantiation.
        - If person is chosen to be infected for first round of simulation, then
            the object should create a Virus object and set it as the value for
            self.infection.  Otherwise, self.infection should be set to None.

    did_survive_infection(self):
        - Only called if infection attribute is not None.
        - Takes no inputs.
        - Generates a random number between 0 and 1.
        - Compares random number to mortality_rate attribute stored in person's infection
            attribute.
            - If random number is smaller, person has died from disease.
                is_alive is changed to false.
            - If random number is larger, person has survived disease.  Person's
            is_vaccinated attribute is changed to True, and set self.infection to None.
    '''

        #is_alive is set to True by default
        # TODO:  Finish this method. Follow the instructions in the class documentation
        # TODO: You will need to decide what parameters you pass into this method based on how you structure your class.
        # for resolve_infection.  If person dies, set is_alive to False and return False.
        # If person lives, set is_vaccinated = True, infection = None, return True.
