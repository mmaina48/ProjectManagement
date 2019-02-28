# for letter in 'python':
#     if letter=='h':
#         continue
#     print(letter,end=" ")
#
#
#
# var=10
# while var >0:
#     var=var-1
#     if var==5:
#         continue
#     print(var)

# My ATM Dummy

# psw="@#s"
#
# while (True):
#     x=input("enter password")
#     if x!=psw:
#         print("Enter Again")
#         continue
#     print("Successfull Login")
#     break
#
# balance = int(input("deposit"))
#
# while balance > 0:
#         withdraw = int(input("enter withdraw amount"))
#         balance = balance - withdraw
#         print("Your Remaining balance KSH:",balance)
#         if balance == 1:
#             break
#
# print("You have insuficient Amout")

# ATM Dummy
def verify_pin(pin):
    if pin == '1234':
        return True
    else:
        return False

def log_in():
    tries = 0
    while tries < 4:
        pin = input('Please Enter Your 4 Digit Pin: ')
        if verify_pin(pin):
            print("Pin accepted!")
            return True
        else:
            print("Invalid pin")
            tries += 1
    print("To many incorrect tries. Could not log in")
    return False

def start_menu():
    print("Welcome to the atm!")
    if log_in():
        balance = int(input("deposit"))

        while balance > 0:
            withdraw = int(input("enter withdraw amount"))
            balance = balance - withdraw
            print("Your Remaining balance KSH:", balance)
            if balance == 1:
                break

        print("You have insuficient Amout")

    print("Exiting Program")

start_menu()


