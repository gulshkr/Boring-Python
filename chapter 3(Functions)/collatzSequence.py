def collatz(number):
    if number % 2 == 0:
        # print(number // 2)
        return number // 2
    elif number % 2 ==1:
        # print(3*number+1)
        return 3*number+1
try:
    user_input = int(input("Enter a number: "))
    while user_input != 1:
        user_input = collatz(user_input)
        print(user_input)
except ValueError:
    print('Please enter an integer')
