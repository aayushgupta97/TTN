print("\n\nQuestion1")
my_string = "Hello Python!"
print(my_string[12] + my_string[-2::-1])

print("\n\nQuestion2")
word = "information"
print(word[2::2])

print("\n\nQuestion 5")
d = {'simple_key':'hello'}
print(d['simple_key'])
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0]) 
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

print("\n\nQuestion 6")
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

print("\n\nQuestion 7")
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set_list5 = set(list5)
print(set_list5)

print("\n\nQuestion 8 ")
print('information'.count('i'))

print("\nquestion 8 with for loop")
count = 0 
for letter in 'information':
    if letter == 'i':
        count = count + 1

print(f"Number of times 'i' appears is: {count}")
