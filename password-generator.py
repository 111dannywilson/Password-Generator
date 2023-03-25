import string
import random

alphabets = string.ascii_letters
digits = string.digits
symbols = string.punctuation

values = []

print("Note, password length should be integers")
print('-------------')


# making user input an integer
def check_input():
    password_length = input("Password length: ")
    try:
        password_length = int(password_length)
    except:
        print('Password length must be an integer')
        exit()
    return password_length


# function for getting a specific type of value
def get_values(module, loop_variable):
    for loop_variable in module:
        values.append(loop_variable)


# function for shuffling values
def shuffle_values(limit):
        shuffled_values = []
        while len(shuffled_values) != len(values):
            all_values = random.choice(values)
            shuffled_values.append(all_values)

        # checking for password length gainst all characters length(shuffled_values)
        if len(shuffled_values) < limit:
            print(f'Lenght is too huge, limit is {len(shuffled_values)}')
            exit()
        else:
            return shuffled_values[0:limit]



# appending all types of values to the values list..
get_values(alphabets, 'alphabet')
get_values(digits, 'digit')
get_values(symbols, 'symbol')


password_limit = check_input()
shuffled_values = shuffle_values(password_limit)

# stringifying shuffled_values(a list)
password = ''.join(map(str, shuffled_values))
print(password)
 
