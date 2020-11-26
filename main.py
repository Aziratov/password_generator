#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
cur_letters = 0
cur_symbols = 0
cur_numbers = 0


# Order of characters randomised:
# 4 letter, 2 symbol, 2 number = g^2jk8&P
chars = nr_letters + nr_symbols + nr_numbers

def ran_letter():
    random_val = random.randint(0, len(letters) - 1)
    return letters[random_val]

def ran_num():   
    random_val = random.randint(0, len(numbers) - 1)
    return numbers[random_val]

def ran_sym():
    random_val = random.randint(0, len(symbols) - 1)
    return symbols[random_val]


result_Val = ""
check = True
while (check): 
    
    random_num = random.randint(0, 2)
    if random_num == 0:
        if cur_letters < nr_letters:
            result_Val += str(ran_letter())
            cur_letters +=1
        
    if random_num == 1:
        if cur_numbers < nr_numbers:
            result_Val += str(ran_num())
            cur_numbers +=1

    if random_num == 2:
        if cur_symbols < nr_symbols:
            result_Val += str(ran_sym())
            cur_symbols+=1

    if(cur_numbers + cur_letters + cur_symbols) == chars:
        check = False

print(f"Your customized password is {result_Val}")



#Order not randomized:
# 4 letter, 2 symbol, 2 number = JduE&!91
# for i in range(0, nr_letters):
#     nr_random = random.randint(0, len(letters) - 1)
#     nr_result += letters[nr_random]

# for i in range(0, nr_numbers):
#     nr_random = random.randint(0, len(numbers) - 1)
#     nr_result += numbers[nr_random]

# for i in range(0, nr_symbols):
#     nr_random = random.randint(0, len(symbols) - 1)
#     nr_result += symbols[nr_random]

# print(f"Your pass is {nr_result}")

# Order of characters randomized:
# 4 letter, 2 symbol, 2 number = g^2jk8&P
