import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus

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
    to the |Virus object| upon instantiation.
    mortality_rate: Float between 0 and 1.  This will be passed
    to the |Virus object| upon instantiation.
    basic_repro_num: Float between 0 and 1.   This will be passed
    to the |Virus object| upon instantiation.
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
            # So you run a loop to create person object with infected set to true.
        -- Once all infected person objects are created, begins creating healthy
            person objects.  To decide if a person is vaccinated or not, generates
            a random number between 0 and 1.  If that number is smaller than
            self.vacc_percentage, new person object will be created with is_vaccinated
            set to True.  Otherwise, is_vaccinated will be set to False.
            # Use a for loop to create a list of person object
                - generate and random number then use an if statement to check if
                that number is smaller than self.vacc_percentage then create new
                person object with is_vaccinated set to True.
        -- Once len(population) is the same as self.population_size, returns population.
            # Make an outside if statement (outside the for loops) that checks if
            len(population) == self.population_size then return population
    '''

    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.population = []
        self.total_infected = 0
        self.current_infected = 0
        self.next_person_id = 0
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)
        self.vacc_percentage = vacc_percentage

        # TODO: Create a Logger object and bind it to self.logger.  You should use this
        # logger object to log all events of any importance during the simulation.  Don't forget
        # to call these logger methods in the corresponding parts of the simulation!
        self.logger = None

        # This attribute will be used to keep track of all the people that catch
        # the infection during a given time step. We'll store each newly infected
        # person's .ID attribute in here.  At the end of each time step, we'll call
        # self._infect_newly_infected() and then reset .newly_infected back to an empty
        # list.
        self.newly_infected = []
        # TODO: Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.

        self.population = self._create_population(initial_infected)

    #def _create_population(self, initial_infected):
        # TODO: Finish this method!  This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).
        # population = []
        # infected_count = 0
        # while len(population) != pop_size:
        #     if infected_count !=  initial_infected:
        #         # TODO: Create all the infected people first, and then worry about the rest.
        #         # Don't forget to increment infected_count every time you create a
        #         # new infected person!
        #         pass
        #     else:
        #         # Now create all the rest of the people.
        #         # Every time a new person will be created, generate a random number between
        #         # 0 and 1.  If this number is smaller than vacc_percentage, this person
        #         # should be created as a vaccinated person. If not, the person should be
        #         # created as an unvaccinated person.
        #         pass
        #     # TODO: After any Person object is created, whether sick or healthy,
        #     # you will need to increment self.next_person_id by 1. Each Person object's
        #     # ID has to be unique!
        # return population
        #-----------------------------Given Instruction for Create Population---------------
        """
        # testing
        population = []
        virus = Virus( "Ebola", 0.70, 0.25)
        num_of_people = 6
        for i in range(0, num_of_people):
            person = Person(i, False, Virus)
            population.append(person)
            person2 = Person(i+6, False, None)
            population.append(person2)
        return population
        """
    def _create_population(self, initial_infected,):
        # Total_infected = initial_infected*self.population_size
        print(f"The initial_infected value is: {initial_infected}")
        self.population = []
        infected_count = 0
        vax_count = 0
        while len(self.population) != self.population_size:
            #Create infected population
            if infected_count !=  initial_infected:
                self.population.append(Person(self.next_person_id,False, self.virus_name))
                print("We created infected people.")
                infected_count += 1
            #Create vax population
            elif vax_count != (self.population_size * self.vacc_percentage):
                self.population.append(Person(self.next_person_id,True, None))
                print("We created vaccinated people.")
                vax_count += 1
            else:
                #Create non-vax non-infected population
                self.population.append(Person(self.next_person_id,False, None))
                print("We created people that are alive.")
            # assigns a new id
            self.next_person_id += 1
            # print(f"Number of people {len(self.population)}")
        return self.population


    def _simulation_should_continue(self):
        # TODO: Complete this method!  This method should return True if the simulation
        # should continue, or False if it should not.  The simulation should end under
        # any of the following circumstances:
        #     - The entire population is dead.
        #     - There are no infected people left in the population.
        # In all other instances, the simulation should continue.
        """
        Pseudocode:
        This method should return a boolean.
            # dead = dies from infection
            # create variable named death_counter set to 0
            # run for loop for each person object in population
                # check if person.is_alive is set to false
                    # if it is increment counter by 1
            # exit loop then check if len(population) equals death_counter
            then return False
            # create variable named vaccinated_counter set to 0
            # run another for loop for each person object in population
                    # check if person.is_vacc == True and person.is_alive == True
                        # if it is increment vaccinated_counter by 1
            # exit loop then check if len(population) equals population_counter
            then return False
            return True
        """
        # EVERYBODY dead
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
            print("No one in the population has the virus!!")
            return False
        # SIMULATION should stop
        print("Simulation will continue to run!!")
        return True

        """
        Another way to structure the code:
        # EVERYBODY dead
        death_counter = 0
        # iterate for entire population
        for person in population:
            # check to see if person is dead
            if person.is_alive == false:
                death_counter += 1
            # if person not dead then check if they are infected
            else:
                # if person is infected and still alive in simulation then
                # continue to run simulation
                # possible use isinstance to check of the person has virus or
                # not: https://www.geeksforgeeks.org/type-isinstance-python/
                if person.infected != None:
                    return True
        if len(population) ==  death_counter:
            return False
        """
        pass


    def run(self):
        # TODO: Finish this method.  This method should run the simulation until
        # everyone in the simulation is dead, or the disease no longer exists in the
        # population. To simplify the logic here, we will use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # This method should keep track of the number of time steps that
        # have passed using the time_step_counter variable.  Make sure you remember to
        # the logger's log_time_step() method at the end of each time step, pass in the
        # time_step_counter variable!
        time_step_counter = 0
        should_continue = self._simulation_should_continue()
        while should_continue:
        # TODO: for every iteration of this loop, call self.time_step() to compute another
        # round of this simulation.  At the end of each iteration of this loop, remember
        # to rebind should_continue to another call of self._simulation_should_continue()!
            self.time_step()
            # Increment the counter by 1 each time
            time_step_counter += 1
            logger.log_time_step(time_step_counter)
            should_continue = self._simulation_should_continue()
        print('The simulation has ended after {} turns.'.format(time_step_counter))


    def time_step(self):
            infected_people = []
            interaction_counter = 0
            # Get infect people from out of the population
            for person in self.population:
                # if person is alive and person has virus
                if person.is_alive == True and person.infection != None:
                    infected_people.append(person)
            # For each infected person in the population
            for infected_person in infected_people:
                # Repeat for 100 total interactions:
                for _ in range(0, 100):
                    # Grab a random person from the population
                    random_index = random.randint(0, len(self.population)- 1)
                    print("An infected person's random index: {}".format(random_index))
                    random_person = self.population[random_index]
                    print("The random person: {} ".format(random_person))
                    # If the person is dead, continue and grab another new
                    # person from the population.
                    if random_person.is_alive == False:
                        continue
                    else:
                        # Call simulation.interaction(person, random_person)
                        self.interaction(infected_person, random_person)
                        # interaction_counter += 1
                        interaction_counter += 1

            # Take care of previous round and now we can run _infect_newly...
            for person in self.population:
                if person.is_alive == True and person.infection != None:
                    # for logger function what this function returns
                    person.did_survive_infection(self.mortality_rate)

            self._infect_newly_infected()


    def interaction(self, person, random_person):
        # TODO: Finish this method! This method should be called any time two living
        # people are selected for an interaction.  That means that only living people
        # should be passed into this method.  Assert statements are included to make sure
        # that this doesn't happen.
        """
        If this code return false this function should not run
        """
        assert person.is_alive == True
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
        """
        Pseudocode:
        if random_person.is_vaccinated == True:
            continue
        if random_person.infected != None:
            continue
        if random_person.is == True and random_person.is_vaccinated
        """
        # Your doing these checks below:
        # if random_person.is_vaccinated == True:
        #     pass
        # # If they are sick they can't get sick again so we don't do anything
        # if random_person.infection != None:
        #     pass
        if random_person.infection == None and random_person.is_vaccinated == False:
            random_num = float(random.randint(0, 100)/100)
            if random_num <= self.basic_repro_num:
                self.newly_infected.append(random_person._id)
        else:
            pass
        # Comment in when you have coded the logger
        #self.logger.log_interaction()

    def _infect_newly_infected(self):
        # TODO: Finish this method! This method should be called at the end of
        # every time step.  This method should iterate through the list stored in
        # self.newly_infected, which should be filled with the IDs of every person
        # created.  Iterate though this list.
        # For every person id in self.newly_infected:
        #   - Find the Person object in self.population that has this corresponding ID.
        #   - Set this Person's .infected attribute to True.
        # NOTE: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list!


        for newly_infected_person_id in self.newly_infected:
            for person in self.population:
                if person._id == newly_infected_person_id:
                    person.infection = True

        self.newly_infected = []


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
