filename=input("Enter the file name which u wanna import to check the specific string is there or not: ") # taking file name as input

try:  #using try except in this code
    with open(filename) as file:   #opening file using user input as file
        print("file exists")       # if file exists compiler prints this
        spe_string=input("Enter the string u want to check: ") # taking user input ...which string they want to find

        def check(filename, spe_string):  # function for searching string and return lines which contain that specific string
            string_address = []           # empty list
            with open(filename) as file:
                for lines in file:        # here i m accessing each line with this for loop
                    if spe_string in lines: #checking that specific string is in which line
                        string_address.append(lines.strip())  # if the string contains that line will append into the string_address list

            return string_address

        if len(check(filename,spe_string))==0: # here checking the length of that function output if it is 0 then it executes
            print("No string is found in the given file.")
        else:# or else this will exexute and prints the ouput as list of lines which contains specific string
            print(check(filename,spe_string))

except FileNotFoundError as error:  # by using except and FileNotFoundError if the file doesn't exist then compiler gives this file doesn't found error
    print(error)






