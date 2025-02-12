print("Hello World!!!")

from random import randint

def generate_class(n):
    return [randint(1,365) for _ in range(n)]
    
print("tell me how many people you want to generate!")
n = input()
n_number = int(n)

print(generate_class(n_number))


