import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print('\n')
print('_________________________________')
print('Vamos gerar uma senha para você !')
print('_________________________________')
print('\n')

n_letters = int(input('Quantas letras você precisa ? '))
n_symbols = int(input('Quantos símbolos você precisa ? '))
n_numbers = int(input('Quantos números você precisa ? '))
print('_________________________________')
print('\n')

for char in range (1, n_letters + 1):
    random_char = random.choice(letters)
    print(random_char)
    
for number in range (1, n_symbols + 1):
    random_symbols = random.choice(symbols)
    print(random_symbols)
    
for char in range (1, n_numbers + 1):
    random_number = random.choice(numbers)
    print(random_number)
    

print('_________________________________')
print('\n')
