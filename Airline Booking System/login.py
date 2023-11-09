#username and password texting
import csv
login = False

with open('Usernames.txt', 'r') as csv_file: #opens file and refers to it as csv_file
    csv_reader = csv.reader(csv_file) #reads the csv file

    next(csv_reader) #skips first line (containing field names)
    
    for line in csv_reader:
        username = line[0]
        password = line[1]
        
    usernameInput = input("what is your username?")
    passwordInput = input("what is your password?")

    for i in range(len(username)):
        if usernameInput == username[0]:
                print ("login successful")


    if login == True:
        print ("You are logged in")
