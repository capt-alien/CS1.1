class Logger(object):

    def __init__(self, file_name):
        # TODO:  Finish this initialization method.  The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

# https://www.pythonforbeginners.com/cheatsheet/python-file-handling
# Also got help from Nolen Kovacik for this one:

    def write_metadata(self, pop_size, vax_percentage, virus_name, mortality_rate, basic_repro_num):
        # writes to text file
        with open(self.file_name, "w") as file:
            file.write(f"{population_size}\t {vax_percentage}\t {virus_name}\t {mortality_rate}\t {infection_rate}")
            file.write("/n========================================================/n")
            file.write(f"     Population Size: {population_size}\n")
            file.write(f"    Vaccination Rate: {vax_percentage}\n")
            file.write(f"          Virus Name: {virus_name}\n" )
            file.write(f"      Mortality Rate: {mortality_rate}\n")
            file.write(f"      Infection Rate: {infection_rate}\n")
            file.write(f" # initial infection: {initial_infected}\n")
            file.write(f"   # of interactions: {interactions}\n")
        file.close()

        #Print same data to consol:
        print(f"     Population Size: {population_size}")
        print("    Vaccination Rate: {vax_percentage}")
        print("          Virus Name: {virus_name}" )
        print("      Mortality Rate: {mortality_rate}")
        print("      Infection Rate: {infection_rate}")
        print(" # initial infection: {initial_infected}")
        print("   # of interactions: {interactions}")



    def log_interaction(self, person1, person2):
        with open(self.file_name, "w") as file:
            # if person1 has the virus then person1 infects person2
            if person1.infection != None:
                file.write(f"/n {person1._id} infects {person2._id} because already sick. /n")
            # if person2 has the virus then person1 infects person2
            if person2.infection != None:
                file.write(f"/n {person2._id} infects {person1._id} because already sick. /n")
            if person1.is_vaccinated == True:
                file.write(f"/n {person1._id} didn't infect {person2._id} because vaccinated. /n")
            if person2.is_vaccinated == True:
                file.write(f"/n {person2._id} didn't infect {person1._id} because vaccinated. /n")
        file.close()


    def log_infection_survival(self, person, population):
        did_die_from_infection = None
        # removed "is_alive" from parmaeters
        with open(self.file_name, "a") as file:
            for person in population:
                if person.is_alive == True:
                    did_die_from_infection == False
                    file.write(f"/n Person ID: {person._id} survived infection and is now immune")
            else:
                did_die_from_infection = True
                file.write(f"/n Person ID: {person._id} died from infection./n")
            file.close()


    def log_time_step(self, time_step_number):
        next_step = int(time_step_number + 1)
        with open(self.file_name, "a") as file:
            file.write("/n ===========================================/n")
            file.write(f"/n Time step {time_step_number} has ended, starting time step {next_step}/n")
            file.write("/n ===========================================/n")
            file.close()
