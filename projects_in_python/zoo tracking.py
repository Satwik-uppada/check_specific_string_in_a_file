# Define an empty dictionary to store the exhibit counts
exhibits = {}

# Define a function to add an animal to an exhibit
def add_animal(animal_name):
    # Check if the exhibit is already in the dictionary
    if animal_name in exhibits:
        exhibits[animal_name] += 1

    else:
        exhibits[animal_name] = 1


# Define a function to remove an animal from an exhibit
def remove_animal(animal_name):
    # Check if the exhibit is already in the dictionary
    if animal_name in exhibits:
        if exhibits[animal_name] > 0:
            exhibits[animal_name] -= 1

        else:
            print("There are no animals in the {} exhibit to remove.".format(animal_name))
    else:
        print("Invalid animal_name.")

# Main loop of the program
while True:
    # Ask the user for an action to perform
    choice= int(input("List of operations "
                       "\nEnter...."
                   "\n '1' To add animal"
                   "\n '2' To remove animal"
                   "\n '3' To view total exhibit"
                   "\n '4' To quit"
                    "\n Enter operation according to your need: "))

    # Perform the selected action
    if choice ==1:
        animal_name= input("Enter the name of animal to add : ")
        add_animal(animal_name)
        print(f"Added 1 animal to the {animal_name} exhibit. Current count: {exhibits[animal_name]}")

    elif choice==2:
        animal_name = input("Enter the name of the exhibit to remove an animal from: ")
        remove_animal(animal_name)
        if animal_name in exhibits:
            print(f"Removed 1 animal from the {animal_name} exhibit. Current count: {exhibits[animal_name]}")

    elif choice==3:
        print("Current count of all exhibits:")
        for animal_name, count in exhibits.items():
            print(f"{animal_name}: {count}")
    elif choice ==4:
        break
    else:
        print("Invalid input.")



