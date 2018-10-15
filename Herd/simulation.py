import random, sys
random.seed(42)
from person import Person
from logger import Logger

def validator_num (input_text, low_num, high_num):
    is_valid = False
    while True:
        try:
            print(low_num)
            print(high_num)
            entry = input(input_text)
            if entry.isdigit() == True and int(entry) > int(low_num) and int(entry) < int(high_num) :
                is_valid = True
                return entry
            else:
                print("Invalid Input! Try again...")
        except:
            print("Error Invalid Input! Try again...")



class Simulation(object):
    '''
    Main class that will run the herd immunity simulation program.  Expects initialization
    parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.

    _____Attributes______

    logger: Logger object.  The helper object that will be responsible for writing
    all logs to the simulation.

    population_size: Int.  The size of the population for this simulation.

    population: [Person].  A list of person objects representing all people in
        the population.

    next_person_id: Int.  The next available id value for all created person objects.
        Each person should have a unique _id value.

    virus_name: String.  The name of the virus for the simulation.  This will be passed
    to the Virus object upon instantiation.

    mortality_rate: Float between 0 and 1.  This will be passed
    to the Virus object upon instantiation.

    basic_repro_num: Float between 0 and 1.   This will be passed
    to the Virus object upon instantiation.

    vacc_percentage: Float between 0 and 1.  Represents the total percentage of population
        vaccinated for the given simulation.

    current_infected: Int.  The number of currently people in the population currently
        infected with the disease in the simulation.

    total_infected: Int.  The running total of people that have been infected since the
    simulation began, including any people currently infected.

    total_dead: Int.  The number of people that have died as a result of the infection
        during this simulation.  Starts at zero.


    _____Methods_____

    __init__(population_size, vacc_percentage, virus_name, mortality_rate,
     basic_repro_num, initial_infected=1):
        -- All arguments will be passed as command-line arguments when the file is run.
        -- After setting values for attributes, calls self._create_population() in order
            to create the population array that will be used for this simulation.

    _create_population(self, initial_infected):
        -- Expects initial_infected as an Int.
        -- Should be called only once, at the end of the __init__ method.
        -- Stores all newly created Person objects in a local variable, population.
        -- Creates all infected person objects first.  Each time a new one is created,
            increments infected_count variable by 1.
        -- Once all infected person objects are created, begins creating healthy
            person objects.  To decide if a person is vaccinated or not, generates
            a random number between 0 and 1.  If that number is smaller than
            self.vacc_percentage, new person object will be created with is_vaccinated
            set to True.  Otherwise, is_vaccinated will be set to False.
        -- Once len(population) is the same as self.population_size, returns population.
    '''

    def __init__(self, population_size, vax_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.population = []
        self.vax_percentage = vax_percentage
        self.total_infected = 0
        self.current_infected = 0
        self.next_person_id = 0
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)

        self.logger = None
        self.newly_infected = []


    def _create_population(self, initial_infected,):
        population = []
        infected_count = 0
        vax_count = 0
        while len(population) != self.population_size:
            #Create infected population
            if infected_count !=  initial_infected:
                self.population.append(Person(self.next_person_id,False, self.virus_name))
                infected_count += 1
            #Create vax population
            elif vax_count != (self.population_size * self.vax_percentage):
                self.population.append(Person(self.next_person_id,True,))
                vax_count += 1
            else:
                #Create non-vax non-infected population
                self.population.append(Person(self.next_person_id,False,))
            # assigns a new id
            self.next_person_id += 1
        return population


    def _simulation_should_continue(self):
                death_counter = 0
        for person in self.population:
            # if not alive
            if person.is_alive == False:
                death_counter += 1
                print("Death counter value: {}".format(death_counter))
        if len(self.population) == death_counter:
            print("Everyone is dead!")
            return False
        # EVERYBODY vaccinated
        not_infected_counter = 0
        for person in self.population:
            # if person does not have a virus and person is alive
            if person.infection == None:  # and person.is_alive == True: <- you filter out people that are dead
                not_infected_counter += 1
        if len(self.population) ==  not_infected_counter:
            print("A good amount of people do not have the virus!!")
            return False
        # SIMULATION should stop
        print("Simulation will continue to run!!")
        return True


    def run(self):
        time_step_counter = 0
        # TODO: Remember to set this variable to an intial call of
        # self._simulation_should_continue()!
        should_continue = self._simulation_should_continue()
        while should_continue:
        # TODO: for every iteration of this loop, call self.time_step() to compute another
        # round of this simulation.  At the end of each iteration of this loop, remember
        # to rebind should_continue to another call of self._simulation_should_continue()!
            self.time_step()
            # Increment the counter by 1 each time
            time_step_counter += 1
            # update the logger's log_time_step method by passing in the
            # time_step_counter
            # Coment in once you create logger:
            # log_time_step(time_step_counter)
            # rebind should_continue to another call of self._simulation_should_continue()
            should_continue = self._simulation_should_continue()
        print('The simulation has ended after {} turns.'.format(time_step_counter))

    def time_step(self):
        # TODO: Finish this method!  This method should contain all the basic logic
        # for computing one time step in the simulation.  This includes:
            # - For each infected person in the population:
            #        - Repeat for 100 total interactions:
            #             - Grab a random person from the population.
            #           - If the person is dead, continue and grab another new
            #                 person from the population. Since we don't interact
            #                 with dead people, this does not count as an interaction.
            #           - Else:
            #               - Call simulation.interaction(person, random_person)
            #               - Increment interaction counter by 1.
            pass

    def interaction(self, person, random_person):
        # TODO: Finish this method! This method should be called any time two living
        # people are selected for an interaction.  That means that only living people
        # should be passed into this method.  Assert statements are included to make sure
        # that this doesn't happen.
        assert person1.is_alive == True
        assert random_person.is_alive == True

        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0 and 1.  If that number is smaller
            #     than basic_repro_num, random_person's ID should be appended to
            #     Simulation object's newly_infected array, so that their .infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Remember to call self.logger.log_interaction() during this method!
        pass

# We are going to have to edit infect newly infected method when I get Marrianna's functions

    def _infect_newly_infected(self):
        #creates a loop to see see if people interacted with infected people
        for person in population:
            if infect_interaction = true and person.is_vaccinated = False:
                #determines random number to base chance off
                infect_chance = random.randint(0,100)
                #infects unlucky person
                if infect_chance <= (virus.reproduction_rate * 100):
                    person.infection = virus.name



        # TODO: Finish this method! This method should be called at the end of
        # every time step.  This method should iterate through the list stored in
        # self.newly_infected, which should be filled with the IDs of every person
        # created.  Iterate though this list.
        # For every person id in self.newly_infected:
        #   - Find the Person object in self.population that has this corresponding ID.
        #   - Set this Person's .infected attribute to True.
        # NOTE: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list!

if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate,
                            basic_repro_num, initial_infected)
    simulation.run()
