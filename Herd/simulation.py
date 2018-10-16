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
        self.logger = Logger(self.file_name)

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
        time_step_counter = 0
        should_continue = self._simulation_should_continue()
        while should_continue:
            self.time_step()
            # Increment the counter by 1 each time
            time_step_counter += 1
            self.logger.log_time_step(time_step_counter)
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
                        self.interaction(infected_person, random_person)
                        interaction_counter += 1

            for person in self.population:
                if person.is_alive == True and person.infection != None:
                    # for logger function what this function returns
                    person.did_survive_infection(self.mortality_rate)
                    self.logger.log_infection_survival(person, self.population)

            self._infect_newly_infected()


    def interaction(self, person, random_person):

        assert person.is_alive == True
        assert random_person.is_alive == True

        if random_person.infection == None and random_person.is_vaccinated == False:
            random_num = float(random.randint(0, 100)/100)
            if random_num <= self.basic_repro_num:
                self.newly_infected.append(random_person._id)
        else:
            pass
        # Comment in when you have coded the logger
        self.logger.log_interaction(person, random_person)

    # def log_interaction(self, person1, person2, did_infect=None, person2_vacc=None, person2_sick=None):


    def _infect_newly_infected(self):
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
