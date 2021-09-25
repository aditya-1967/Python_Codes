import random
import time


print("******************************** Welcome to the game ********************************\n\n")
print("******************************** This game has 5 rounds ********************************")
print("Enter 'r' for 'Rock', 'p' for 'Paper' and 's' for 'Scissors'")





ask = "y"

while(ask == "y"):
    
    result_user = []
    result_comp = []
    comp_choice = ['r', 'p', 's']
    count = 1

    while(count <= 5):
        choice = input("Your Turn: ")
        comp_turn = random.choice(comp_choice)

        if choice == 'r':
            if comp_turn == 'p':
                result_user.append(0)
                result_comp.append(1)
            elif comp_turn == 's':
                result_user.append(1)
                result_comp.append(0)
            else:
                result_user.append(0)
                result_comp.append(0)

        if choice == 's':
            if comp_turn == 'p':
                result_user.append(1)
                result_comp.append(0)
            elif comp_turn == 'r':
                result_user.append(0)
                result_comp.append(1)
            else:
                result_user.append(0)
                result_comp.append(0)

        if choice == 'p':
            if comp_turn == 'r':
                result_user.append(1)
                result_comp.append(0)
            elif comp_turn == 's':
                result_user.append(0)
                result_comp.append(1)
            else:
                result_user.append(0)
                result_comp.append(0)

        count += 1

    sum_user = 0
    sum_comp = 0

    for i in result_user:
        sum_user += i

    for j in result_comp:
        sum_comp += j

    if sum_user > sum_comp:
        print(f'User Score: {sum_user}\nComp Score: {sum_comp}\nUser Wins')
    elif sum_user <sum_comp:
        print(f'User Score: {sum_user}\nComp Score: {sum_comp}\nComputer Wins')
    else:
        print(f'User Score: {sum_user}\nComp Score: {sum_comp}\nIt is a tie')

    ask = input("Do you want to play another round? (y/n): ")
    
print("Thankyou for playing!")
time.sleep(2)
print("Exiting...")

