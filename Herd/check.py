
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


result = validator_num("test question? ", 0, 100)









	def write_metadata(self, population_size, vaccination_rate, virus_name, mortality_rate, infection_rate, initial_infected, num_interactions):
		# Open file from the simulation
		with open(self.file_name, "w") as file:
			# Write parameters to first line of file
			file.write(f"{population_size}\t{vaccination_rate}\t{virus_name}\t{mortality_rate}\t{infection_rate}\n")
			file.write("\n=========================\n")
			file.write(f" population_size: {population_size}\n")
			file.write(f"vaccination_rate: {vaccination_rate}\n")
			file.write(f"      virus_name: {virus_name}\n")
			file.write(f"  mortality_rate: {mortality_rate}\n")
			file.write(f"  infection_rate: {infection_rate}\n")
			file.write(f"initial_infected: {initial_infected}\n")
			file.write(f"num_interactions: {num_interactions}\n\n")

		# Close file when done
		file.close()
