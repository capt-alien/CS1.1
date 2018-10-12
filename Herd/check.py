
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
