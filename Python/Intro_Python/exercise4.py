# generate all even numbers upto 100 also divisible by 5

my_list = [i for i in range(5,101) if i%5==0 and i%2==0]
print(my_list)


#Question 1
a = int(input("Enter the max number: "))

def fib(n):
    a , b = 0 , 1 
    while(a<n) : 
        yield a 
        a , b = b , a + b 
print(list(fib(a)))


# def fibGen(N): 
#     n1 = 0
#     n2 = 1
#     while(n1 + n2 < N):
#         n3 = n1+ n2
#         yield n3
#         n1= n2
#         n2 = n3

# # fibnums = fibGen(30)
# # print(list(fibnums))

# for fib in fibGen(30):
#     print(fib)

def gen_fib_with_len(L):
    
    count, n1, n2 = 0, 0, 1
    while count < L:
        yield n1
        next_fib = n1+n2
        n1, n2 = n2, next_fib
        count += 1
L = int(input('Set the length of the generator Fibonacci sequence: '))
print(list(gen_fib_with_len(L)))

#Question 2
# def decorator_function(func) 
def call_twice(func):
        def inner():
                func()
                func()
        return inner

@call_twice
def say_hi():
        print("hi")
@call_twice
def say_bye():
        print("bye")
say_hi()
say_bye()

# Question 3
from collections import Counter

with open('sample.txt', 'r') as myfile:
    data = myfile.read()
    print(data)
    count = Counter(data.split())
    # print(count.most_common())
    print(count.most_common()[0])

# Question 4
from math import ceil, sqrt

def gen_prime():
    num = 2
    while input("Enter 'y' for next prime, or any other key to exit: ") == 'y':
        yield num
        found = False
        while not found:
            found = True
            num += 1
            max_div = int(ceil(sqrt(num))) + 1
            for div in range(2, max_div):
                if num % div == 0:
                    found = False
                    break


for prime in gen_prime():
    print(prime)
# print(list(gen_prime()))


# Question 5
def conversion(digit, unit1, unit2):
	unit = {'km': 1000,
			'm':1,
			'cm':0.01,
			'mm' : 0.001}

	return digit * (unit[unit1] / unit[unit2])

print("Use km for kilometers\nUse m for metres\nUse cm for centimeters\nUse mm for milimeters")
unit1 = input("Enter the unit you want to use: ")
unit2 = input("Enter the unit you want to convert to: ")

digit = float(input("Enter the value to convert: "))
output = conversion(digit, unit1, unit2)
print(output)
