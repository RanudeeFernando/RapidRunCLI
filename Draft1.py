import random

print("Welcome to 'Rapid Run' Horse Race Management System!")

print('''
COMMANDS:
• Type AHD for adding horse details.
• Type UHD for updating horse details.
• Type DHD for deleting horse details.
• Type VHD for viewing the registered horses’ details table.
• Type SHD for saving the horse details to the text file.
• Type SDD for selecting four horses randomly for the major round.
• Type START to start the race.
• Type WHD for displaying the Winning horses’ details.
• Type VWH for Visualizing the time of the winning horses.
• Type ESC to exit the program.

NOTE:
• Please execute the AHD, UHD, and DHD commands before attempting to START the race.
• Please execute the SHD, SDD, WHD, and VWH commands in this order to generate accurate results.
• Please START the race in order to execute the WHD and VWH commands. 
''')

registered_horses = []
race_horses = []
winners = []

horse_count = 0
start_command_count = 0
selecting_horses_count = 0
selecting_time_count = 0
appending_winners_count = 0
displaying_whd_count = 0

race_started = False


# Defining a function for Adding Horse Details (AHD)
def ahd():
    def register_horse():
        horse_details = {}

        while True:
            horse_id = input('Enter Horse ID: ')
            try:
                if not int(horse_id):
                    raise ValueError

                elif horse_id in [registered_horse['Horse ID'] for registered_horse in registered_horses]:
                    print('This Horse ID already exists. Please enter a unique Horse ID!')
                    continue

                else:
                    horse_details['Horse ID'] = horse_id
                    break

            except ValueError:
                print("This ID format is invalid. For instance, use '001' as a proper format.")
                continue

        horse_name = input('Enter Horse Name: ')
        horse_details['Horse Name'] = horse_name

        jockey_name = input('Enter Jockey Name: ')
        horse_details['Jockey Name'] = jockey_name

        while True:
            try:
                age = int(input('Enter Age: '))
                horse_details['Age'] = str(age) + ' years'
                break
            except ValueError:
                print('Please enter a valid integer for Age.')
                continue

        breed = input('Enter Breed: ')
        horse_details['Breed'] = breed

        race_record = input('Enter Race Record: ')
        horse_details['Race Record'] = race_record

        while True:
            group = input('Enter Group (A/B/C/D): ').upper()
            if group not in ['A', 'B', 'C', 'D']:
                print('The group you entered is invalid. Please select a group from A, B, C, or D!')

            else:
                horse_details['Group'] = group
                break

        return horse_details

    global registered_horses
    global horse_count
    global race_started

    if not race_started:
        if horse_count < 20:
            new_horse = register_horse()
            new_horse_id = new_horse['Horse ID']
            registered_horses.append(new_horse)
            horse_count += 1
            print(f"Horse '{new_horse_id}' has successfully been registered!")

        else:
            print('\nYou have reached the maximum limit for Registered Horses.')
            print('You cannot register more horses beyond this limit.')

    else:
        print('Sorry, the registration is closed. The race has already started.')


# Defining a function for Updating Horse Details (UHD)
def uhd():
    global registered_horses
    global race_started

    if not race_started:
        # if registered_horses list is empty this code block will be executed
        if not registered_horses:
            print(f"No horses have been registered yet. Please register horses before attempting to update their details.")

        # if registered_horses list is not empty this code block will be executed
        else:
            uhd_horse_id = input('Enter Horse ID to update horse details: ')
            horse_updated = False  # Flag is added to avoid having an ELSE condition in the FOR loop
            for registered_horse in registered_horses:
                while uhd_horse_id == registered_horse['Horse ID']:

                    print('\nType 1 to update Horse Name')
                    print('Type 2 to update Jockey Name')
                    print('Type 3 to update Age')
                    print('Type 4 to update Breed')
                    print('Type 5 to update Race Record')
                    print('Type 6 to update Group\n')

                    update_detail_choice = input('Enter the horse detail you wish to update: ')

                    if update_detail_choice == '1':
                        updated_horse_name = input('Update Horse Name to: ')
                        registered_horse['Horse Name'] = updated_horse_name
                        print(f"Horse Name of Horse '{uhd_horse_id}' has been updated to '{updated_horse_name}'.")
                        horse_updated = True
                        break

                    elif update_detail_choice == '2':
                        updated_jockey_name = input('Update Jockey Name to: ')
                        registered_horse['Jockey Name'] = updated_jockey_name
                        print(f"Jockey Name of Horse '{uhd_horse_id}' has been updated to '{updated_jockey_name}'.")
                        horse_updated = True
                        break

                    elif update_detail_choice == '3':
                        while True:
                            try:
                                updated_age = int(input('Update Age to: '))
                                registered_horse['Age'] = str(updated_age) + ' years'
                                print(f"Age of Horse '{uhd_horse_id}' has been updated to '{updated_age} years'.")
                                horse_updated = True
                                break
                            except ValueError:
                                print('Please enter a valid integer for Age.')
                                continue
                        break

                    elif update_detail_choice == '4':
                        updated_breed = input('Update Breed to: ')
                        registered_horse['Breed'] = updated_breed
                        print(f"Breed of Horse '{uhd_horse_id}' has been updated to '{updated_breed}'.")
                        horse_updated = True
                        break

                    elif update_detail_choice == '5':
                        updated_race_record = input('Update Race Record to: ')
                        registered_horse['Race Record'] = updated_race_record
                        print(f"Race Record of Horse '{uhd_horse_id}' has been updated to '{updated_race_record}'.")
                        horse_updated = True
                        break

                    elif update_detail_choice == '6':
                        while True:
                            updated_group = input('Update Group to: ').upper()
                            if updated_group in ['A', 'B', 'C', 'D']:
                                registered_horse['Group'] = updated_group
                                print(f"Group of Horse '{uhd_horse_id}' has been updated to '{updated_group}'.")
                                horse_updated = True
                                break
                            else:
                                print('Invalid Group. Please select a group from A, B, C, or D.')
                                continue
                        break

                    else:
                        print('Invalid response. Please enter a number from 1-6 to update the relevant details.')
                        continue

            # if registered_horses list does not include entered horse ID this code block will be executed
            if not horse_updated:
                print(f"Horse '{uhd_horse_id}' does not exist. Please enter a registered Horse ID to update horse details!")

    else:
        print('Sorry, you cannot update horse details. The race has already started.')


# Defining a function to Delete Horse Details (DHD)
def dhd():
    global race_started
    global registered_horses
    global horse_count

    if not race_started:
        # if registered_horses list is not empty this code block will be executed
        if not registered_horses:
            print('No horses have been registered yet. Please register a horse before attempting to delete its details.')

        else:
            # if registered_horses list is not empty this code block will be executed
            dhd_horse_id = input('Enter Horse ID to delete horse details: ')

            horse_deleted = False  # Flag is added to avoid the print statements in FOR loop from repeating
            for registered_horse in registered_horses:
                if dhd_horse_id == registered_horse['Horse ID']:
                    registered_horses.remove(registered_horse)
                    horse_deleted = True
                    horse_count -= 1
                    print(f"Details of horse '{dhd_horse_id}' have successfully been deleted!")

            # if registered_horses list does not include entered horse ID this code block will be executed
            if not horse_deleted:
                print(f"Horse '{dhd_horse_id}' does not exist. Please enter a registered Horse ID!")

    else:
        print('Sorry, you cannot delete horse details. The race has already started.')


# Defining a function to View Horse Details (VHD)
def vhd():
    global registered_horses

    # Sorts registered_horses list using selection sort
    # Sorts horses by their Horse ID in ascending order
    for i in range(len(registered_horses)):
        min_index = i
        for j in range(i + 1, len(registered_horses)):
            if int(registered_horses[j]['Horse ID']) < int(registered_horses[min_index]['Horse ID']):
                min_index = j

        # Swap horse at 'i' with the horse at 'min_index'
        registered_horses[i], registered_horses[min_index] = registered_horses[min_index], registered_horses[i]

    # this code block will be executed if registered_horses list is empty
    if not registered_horses:
        print('No horses have been registered yet.')

    # this code block will be executed if registered_horses list is not empty
    else:
        print('Here are the horse details of registered horses sorted in ascending order by their Horse ID:\n')

        for registered_horse in registered_horses:
            horse_details = ', '.join(f'{k}: {v}' for (k, v) in registered_horse.items())
            print(horse_details)
        print()


# Defining a function to Save Horse Details (SHD)
def shd():
    global registered_horses
    grouped_horses = {'A': [], 'B': [], 'C': [], 'D': []}

    # Sorts registered_horses list using selection sort
    # Sorts horses by their Horse ID in ascending order
    for i in range(len(registered_horses)):
        min_index = i
        for j in range(i + 1, len(registered_horses)):
            if int(registered_horses[j]['Horse ID']) < int(registered_horses[min_index]['Horse ID']):
                min_index = j

        # Swap horse at 'i' with the horse at 'min_index'
        registered_horses[i], registered_horses[min_index] = registered_horses[min_index], registered_horses[i]

    # Grouping horses by their group
    for registered_horse in registered_horses:
        group = registered_horse.get('Group')
        grouped_horses[group].append(registered_horse)

    # Code block will be executed if registered_horses list is empty
    if not registered_horses:
        print(f'Text file was created but no horses have been registered yet.')
        print('Please register a horse in order to save details to the text file!')

        # Creates empty text file with no registered horses
        # Overwrites the old text file if registered horses were deleted

        with open('horse_details.txt', 'w') as f:
            for (k1, v1) in grouped_horses.items():
                f.write(f'Group {k1} :\n')
                for horse in v1:
                    horse_details = ', '.join(f'{k2}: {v2}' for (k2, v2) in horse.items())
                    f.write(horse_details)
                    f.write('\n')  # Added to separate horse
                f.write('\n')  # Added for clarity

    # Code block will be executed if registered_horses list is not empty
    else:
        with open('horse_details.txt', 'w') as f:
            for (k1, v1) in grouped_horses.items():
                f.write(f'Group {k1} :\n')
                for horse in v1:
                    horse_details = ', '.join(f'{k2}: {v2}' for (k2, v2) in horse.items())
                    f.write(horse_details)
                    f.write('\n')  # Added to separate horse
                f.write('\n')  # Added for clarity

        print(f"Horse Details have been successfully saved to file '{f.name}'")


# Defining a function for selecting four horses randomly for the major round (SDD)
# This function is divided into two sub functions

# 1. Defining a function for selecting random horses (sub function under SDD)

def selecting_random_horses():
    grouped_horses = {'A': [], 'B': [], 'C': [], 'D': []}
    file_read = False
    randomly_selected_horses = {}

    try:
        # Reading the text file with saved horse details and extracting data
        with open('horse_details.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('Group'):
                    group = line.split()[1]
                elif line:
                    horse_details = line.split(', ')  # horse_details is a list that has the elements in a line which are split by ', '
                    grouped_horses[group].append(horse_details)

            file_read = True

    except FileNotFoundError:
        print(f"The file was not found. Please save the horse details to a text file first to proceed with SDD.")

    # To avoid getting errors if file was not found because {f.name} is used in this code block
    # This code block is executed only if the file was read
    if file_read:
        for group, horses in grouped_horses.items():
            if len(horses) == 5:
                randomly_selected_horses[group] = random.choice(horses)

            else:
                print(f"Please ensure that Group {group} has 5 registered horses that were saved to '{f.name}'.")
                print(f"Please register horses accordingly and save them to '{f.name}' in order to proceed with SDD.\n")

    return randomly_selected_horses


# 2. Defining a function for displaying selected horses (sub function under SSD)

def displaying_selected_horses(randomly_selected_horses):
    global selecting_horses_count

    # This code block would only be executed if all 4 groups have a randomly selected horse
    if len(randomly_selected_horses.values()) == 4:

        if selecting_horses_count < 1:
            for group, horse in randomly_selected_horses.items():
                print(f"Randomly Selected Horse's Details from Group {group}:")
                for i in range(len(horse)):
                    print(horse[i])
                print()

            selecting_horses_count += 1

        else:
            print('You have already selected 4 horses for this round!')


# Defining a function to start the race
def start():
    global race_started
    global start_command_count
    if start_command_count < 1:
        race_started = True
        start_command_count += 1
        print('The race has started!')

    else:
        print('The race has already started. You cannot start again!')


# Defining a function to display Winning Horse Details (WHD)
def whd(randomly_selected_horses):
    global race_horses
    global winners
    global race_started
    global selecting_time_count
    global appending_winners_count
    global displaying_whd_count
    if race_started:

        # The AND conditions are used to avoid assigning race_horses multiple race times and to ensure that 4 horses were selected
        if selecting_time_count < 1 and selecting_horses_count == 1:
            for group, horse in randomly_selected_horses.items():
                race_time = random.randint(1, 9) * 10
                horse.append(race_time)
            race_horses = [horse for group, horse in randomly_selected_horses.items()]
            selecting_time_count += 1

        if len(race_horses) == 4:
            # sorting the horses in ascending order according to race_time
            for i in range(len(race_horses)):
                min_index = i
                for j in range(i + 1, len(race_horses)):
                    if race_horses[j][-1] < race_horses[min_index][-1]:  # Assuming race time is the last element
                        min_index = j
                race_horses[i], race_horses[min_index] = race_horses[min_index], race_horses[i]

            print('Displayed below are the details of the winning horses: ')

            places = ['1st', '2nd', '3rd']
            for i in range(len(race_horses) - 1):
                place = places[i]
                horse_id = race_horses[i][0][10:]           # race_horses[i][0] structure is 'Horse ID: ###'
                horse_name = race_horses[i][1][12:]         # race_horses[i][1] structure is 'Horse Name: ###'
                jockey_name = race_horses[i][2][13:]        # race_horses[i][0] structure is 'Jockey Name: ###'
                age = race_horses[i][3][5:]                 # race_horses[i][0] structure is 'Age: ###'
                breed = race_horses[i][4][7:]               # race_horses[i][0] structure is 'Breed: ###'
                race_record = race_horses[i][5][13:]        # race_horses[i][0] structure is 'Race Record: ###'
                horse_group = race_horses[i][6][7:]         # race_horses[i][0] structure is 'Group: ###'
                time = race_horses[i][-1]
                print(f"{place} Place: Horse '{horse_id}' ({time}s)")
                print(f"{horse_name} is a {breed} with jockey {jockey_name} in the saddle from Group {horse_group}.")
                print(f"At the age of just {age}, {horse_name} holds a previous race record of {race_record}.")
                print()
            displaying_whd_count += 1

            if appending_winners_count == 0:
                # There is only one set of winners (3 horses)
                # To limit the winners list to only 3 horses this while loop was added
                for i in range(len(race_horses) - 1):
                    winners.append(race_horses[i])
                appending_winners_count += 1

    else:
        print("Please start the race in order to display winning horses' details!")


# Defining a function to Visualize Winning Horses (VWH)
def vwh():
    global winners
    global displaying_whd_count
    global race_started
    places = ['1st', '2nd', '3rd']

    if race_started and displaying_whd_count > 0:

        # FOR loop to display required details of winners[0], winners[1], and winners[2]
        for i in range(len(winners)):
            horse_id = winners[i][0][10:]
            race_time = winners[i][-1]
            num_asterisks = int(race_time / 10)  # To avoid getting float values variable is converted to int()
            place = places[i]
            print(f"Horse '{horse_id}': {'*' * num_asterisks}{' ' * (9 - num_asterisks)} {race_time}s ({place} Place)")

    else:
        print('Please start the race and use the WHD command first in order to visualize winning horses.')


# Defining a function to Quit The Program (ESC)
def esc():
    print('You have exited the program. See you next time!')


# MAIN COMMAND LINE

selected_horses = None  # To ensure that the selected_horse variable exists in the scope of the entire loop

while True:
    command = input('\nEnter a command: ').lower()
    if command == 'start':
        try:
            if len(selected_horses.values()) == 4:
                start()

            # This code block will be executed if the selected_horses dictionary has less than 4 values
            else:
                print('Before starting the race, please ensure that each of the 4 groups has a randomly selected horse.')
                print('To guarantee this, please execute commands in the following order: AHD, UHD/DHD, SHD, SDD')

        # This code block will be executed if the selected_horses dictionary does not exist
        except AttributeError:
            print('Before starting the race, please ensure that each of the 4 groups has a randomly selected horse.')
            print('To guarantee this, please execute commands in the following order: AHD, UHD/DHD, SHD, SDD')

    elif command == 'ahd':
        ahd()

    elif command == 'uhd':
        uhd()

    elif command == 'dhd':
        dhd()

    elif command == 'vhd':
        vhd()

    elif command == 'shd':
        shd()

    elif command == 'sdd':
        selected_horses = selecting_random_horses()
        displaying_selected_horses(selected_horses)

    elif command == 'whd':
        whd(selected_horses)

    elif command == 'vwh':
        vwh()

    elif command == 'esc':
        esc()
        break

    else:
        print('Invalid command. Please try again!')
