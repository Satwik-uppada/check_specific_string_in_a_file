play = input("Do u wanna play game?(yes/no)\n")
if play != "yes":
    quit()
else:
    print("Okay! Let's play ...")

    approval = int(input("Click '5' to start  the Quiz...or click on '2' to exit ::"))
    if approval == 5:
        print("Let's Go!")
    elif approval == 2:
        quit()
    else:
        print("please choose correct option...")
        leave = input("Do u wanna exit?(yes/no) ")
        if leave == "yes":
            quit()
        else:
            approval1 = int(input("if u wanna play click '5'... "))
            if approval1 == 5:
                print('Let\'s Go!')
            else:
                confirm = int(input("Plz select only '5' to start or other numbers to exit.."))
                if confirm == 5:
                    print("Let's play  :)")
                else:
                    quit()
    print("Let's start with yes/no questions")
    score = 0
    answer = input("Q1.Is python is a interpret language? ")
    if answer == "yes":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("Q2.Is python is a coding language? ")
    if answer == "yes":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("Q3.Is python is machine dependant? ")
    if answer == "no":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("Q4.Is python is most using programming language? ")
    if answer == "yes":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("your score is: ", score)
