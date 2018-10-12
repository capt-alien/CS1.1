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
