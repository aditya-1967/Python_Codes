import random

length = (int)(input("Enter the lenght of password to be generated: "))

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
low_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

temp_pass_list = []
password = []

combined_list = digits + low_case + uppercase + symbols

for i in range(10):
    temp_digits = random.choice(digits) 
    temp_low_case = random.choice(low_case) 
    temp_uppercase = random.choice(uppercase)
    temp_symbols = random.choice(symbols)

    temp_pass = temp_digits + temp_uppercase + temp_symbols + temp_low_case
    

    for i in range(length - 4):
        temp_pass += random.choice(combined_list)
        temp_pass_list.append(temp_pass)

for i in temp_pass_list:
    if(len(i) == length):
        password.append(i)
print("\nHere is the Password list to choose from:\n")
print(password)
