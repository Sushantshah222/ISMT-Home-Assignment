# 1. Create a list of the first 10 positive integers. Write a for loop that calculates and prints the sum of all numbers in the list.
list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in range (10):
    sum = sum + list[i]
    print(sum)

#2. Create a list of your five favorite movies. Write a for loop that prints each movie along with its position in the list (e.g., "1. Inception").

my_list = [] 
for i in range(5):  
    names = input("Enter the names of 5 movies")
    my_list.append(names) 
for i, movie in enumerate(my_list, start=1): 
    print(f"{i}. {movie}")

# 3. Given a list of strings representing decimal numbers (e.g., ['1.1', '2.2', '3.3']), write a for loop that converts each string to a float, doubles the value, and prints the result.

list = ['1.1', '2.2', '3.3']
for i in range(len(list)):
    i = float(i)
    i = i * 2
    print(i)

# 4. Create a list of numbers from 1 to 20. Write a for loop that iterates through the list, converts each number to a string, and creates a new list with these string values. Print the new list.
my_list = list(range(1,21))
new = []
for i in my_list:
    i = str(my_list)
    new.append(i)
print(new)

# 5. ⁠WAP that asks 10 user with their name and store them in a list. Print the name of only those users whose name starts with ‘a’ or ‘A’
name = []
for i in range(10):
    n = input("Enter your name ")
    name.append(n)
for j in name:
    if(j[0] == "a" or j[0] == "A"):
        print(j)



# 6. ⁠WAP that asks 10 user with their name and store them in a list. Print the name of only those users whose name ends with ‘a’ or ‘A’
name = []
for i in range(10):
    store = input("Enter the names")
    name.append(store)
for j in name:
    if(j[-1] == "a" or j[-1] == "A"):
        print(j)

    





