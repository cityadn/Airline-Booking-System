import random
import string
import hashlib
import csv

first_name = input("Enter your first name:\n")
last_name = input("Enter your last name:\n")

def userNames(first_name, last_name):
    #this function sets the user name for the user using their first and last name
    #the user name consists of four parts
    #first part = the first letter of the user's first name
    #second part = a random letter in the first name (except the first letter as it is taken)
    #third part = a random letter in the last name (except the first letter)
    #fourth part = first letter of the user's last name
    #these are added together to create the final username in a lower case format
    first = first_name[0]
    
    second_index = random.randint(1, len(first_name) - 1)
    third_index = random.randint(1, len(last_name) - 1)
    
    second = first_name[second_index]
    third = last_name[third_index]
    
    fourth = last_name[0]
    
    user_name = first + second + third + fourth
    user_name = user_name.lower()
    return user_name

def password_database():
    #for the alphabet we decided to obtain a list of ascii characters
    #for the 1st, 2nd, 3rd, 5th, 6th, 7th letters, we pick a random letter in the alphabet list
    #for the 4th character, a random number between 0 and 9 is selected
    #for the 8th character, a special character is selected from the ones in the special character list
    #the password is encrypted using the hashlib library
    alphabet_lst = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    special_char = ['"', '!', '#', '%']

    first_three_one_index = random.randint(0, len(alphabet_lst) - 1)
    first = alphabet_lst[first_three_one_index]

    first_three_two_index = random.randint(0, len(alphabet_lst) - 1)
    second = alphabet_lst[first_three_two_index]

    first_three_three_index = random.randint(0, len(alphabet_lst) - 1)
    third = alphabet_lst[first_three_three_index]

    fourth = random.randint(0, 9)

    first_three_five_index = random.randint(0, len(alphabet_lst) - 1)
    fifth = alphabet_lst[first_three_five_index]

    first_three_six_index = random.randint(0, len(alphabet_lst) - 1)
    sixth = alphabet_lst[first_three_six_index]

    first_three_seven_index = random.randint(0, len(alphabet_lst) - 1)
    seventh = alphabet_lst[first_three_seven_index]

    eight_index = random.randint(0, len(special_char) - 1)
    eighth = special_char[eight_index]

    password = first, second, third, fourth, fifth, sixth, seventh, eighth
    password = (' '.join([str(i) for i in password])).replace(" ", "")

    encrypted_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return encrypted_password, password

encrypted_password, password = password_database()
user_name = userNames(first_name, last_name)
    
print(userNames(first_name, last_name))

login = False

def login_function(login):
    #function does not work with the main code, but it does work on it's own as a single function
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

print(login_function(login))

"""
FC - FIRST CLASS
SD - STANDARD FARE
ER - EXTRA ROOM
IF - INFANT FARE
"""

def seating_area_function():
    seating_area = [['FC','||','FC','||','FC','||'], 
                    ['||','FC','||','FC','||','FC'],
                    ['SD','ER','||','||','ER','SD'],
                    ['SD','||','SD','||', 'SD','||'],
                    ['||','SD','||','SD', '||','SD'],
                    ['SD','||','SD','||', 'SD','||'],
                    ['ER','||','ER','||', 'ER','||'],
                    ['||','IF','||','IF', '||','IF'],
                    ['IF','||','IF','||', 'IF','||'],]
    return seating_area

continue_or_not = 1
seating_area = seating_area_function()
seating_area_function()
for seating_row in seating_area:
    print(seating_row)

customers = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
booked_or_isle_sections = [seating_area[0][1], seating_area[0][3], seating_area[0][5],
                               seating_area[1][0], seating_area[1][2], seating_area[1][4],
                               seating_area[2][2], seating_area[2][3],
                               seating_area[3][1], seating_area[3][3], seating_area[3][5],
                               seating_area[4][0], seating_area[4][2], seating_area[4][4],
                               seating_area[5][1], seating_area[5][3], seating_area[5][5],
                               seating_area[6][1], seating_area[6][3], seating_area[6][5],
                               seating_area[7][0], seating_area[7][2], seating_area[7][4],
                               seating_area[8][1], seating_area[8][3], seating_area[8][5],
                               ]
total_revenue = 0

while continue_or_not == 1:
    def customer_seat_choice(customers, seating_area, row, seat, booked_or_isle_sections):
        #allows the user to book a seat from the seating area list...
        #...without the seats that are classes as isles or booked by other users
        seat_specified = seating_area[row-1][seat-1] #subtracts 1 from the user's choices of row and seats as the user may not know that index ranges in python start from 0, not 1
        while seat_specified in booked_or_isle_sections:
            #this while loop is here in case the user picks a seat that is an isle or one that is booked already
            #repeats until the user picks a free seat
            row = int(input("Out of the 9 rows in our seating area, which row would you like to book?\n"))
            seat = int(input("Out of the 6 seats you have on that row, which seat would you like to book?\n"))
            seat_specified = seating_area[row-1][seat-1]
        booked = "@" + customer.upper() #adds the symbol '@A, for example' to the seat that the user wants to book
        seating_area[row-1][seat-1] = seating_area[row-1][seat-1] + booked
        return seating_area # returns the seating area list with the booked seats

    customer = input("What is your Customer ID? (Letter):\n")
    row = int(input("Out of the 9 rows in our seating area, which row would you like to book?\n"))
    seat = int(input("Out of the 6 seats you have on that row, which seat would you like to book?\n"))

    final_seats = customer_seat_choice(customers, seating_area, row, seat, booked_or_isle_sections)

    def release_seat(booked_or_isle_sections, customers, final_seats):
        #allows the user to unbook seats
        row = int(input("Out of the 9 rows in our seating area, which row would you like to release from your booking?\n"))
        seat = int(input("Out of the 6 seats you have on that row, which seat would you like to release from your booking?\n"))
        booked_symbol = '@' + customer.upper()
        if booked_symbol in final_seats[row-1][seat-1]:
            final_seats[row-1][seat-1] = final_seats[row-1][seat-1].replace(booked_symbol, '') #removes the booked symbol '@A for example' from the seat specified
            return final_seats
        else:
            return final_seats

    print(release_seat(booked_or_isle_sections, customers, final_seats))
    print("\n")

    for seating_row in final_seats:
        print(seating_row)
        #displays the seating area in a clear manner, every isle of the plane being displayed in a new line

    continue_or_not = int(input("Would you like to continue with booking your seats? (1 = yes, 0 = no)\n"))

    def remaining_seats(final_seats, customer, booked_or_isle_sections):
        #shows the user the amount of seats that are left in the plane to be booked
        count = 0
        booked_symbol = '@' + customer.upper()
        for i in range(0, len(final_seats)):
            for j in range(0, len(final_seats[i])):
                if (booked_symbol in final_seats[i][j]) or (final_seats[i][j] in booked_or_isle_sections): #since the seating area is a 2d list, the row and column must be called
                    count = count + 0
                else:
                    count = count + 1
        return count

    print(remaining_seats(final_seats, customer, booked_or_isle_sections))

    def get_revenue(total_revenue, final_seats, customer):
        #calculates the total revenue that is retained from the amount of booked seats there are
        SD = 70
        FC = SD * 10
        ER = SD * 1.1
        IF = SD * 0.1
        booked = '@' + customer.upper()
        for i in range(0, len(final_seats)):
            for j in range(0, len(final_seats[i])):
                    if booked in final_seats[i][j]:
                        if final_seats[i][j] == ("SD" + booked):
                           total_revenue += SD
                        elif final_seats[i][j] == ("FC" + booked):
                            total_revenue+= FC
                        elif final_seats[i][j] == ("ER" + booked):
                            total_revenue += ER
                        elif final_seats[i][j] == ("IF" + booked):
                            total_revenue += IF
        return total_revenue
                
print(get_revenue(total_revenue, final_seats, customer))

total = get_revenue(total_revenue, final_seats, customer) # was going to be used to calculate the average   


    



