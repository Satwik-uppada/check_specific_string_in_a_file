try:
    with open("satwik") as file:
        read_data=file.read()
        print(read_data)
except FileNotFoundError as error:
    print(error)
    print("Could not open satwik.txt")