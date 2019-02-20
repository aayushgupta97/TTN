print("\nQuestion 1")
for i in range(7) :
    if i == 3 or i==6: 
        continue
    print(i)

print("\n\nQuestion 2")
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

result = [[row * col for col in range(n)] for row in range(m)]
print(result)

print("\n\nQuestion 3")
my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = list(filter(lambda x: x%2==0 , my_list))
print(new_list)

print("\n\nQuestion 4")
my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = list(map(lambda x : x**2 , my_list))
print(new_list)


print("\n\nQuestion 5")
Test_data =  [ {"name" : "abhi", "age" : 22}, { "name" : "vikas", "age" : 21} ]

for i in range(len(Test_data)):
    print(f"name {Test_data[i]['name']}\nage : {Test_data[i]['age']}")
