#1. Create a list of the first 10 positive integers. Write a for loop that calculates and prints the sum of all numbers in the list.
x=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in x:
    sum+=i
print(sum)


#2. Create a list of your five favorite movies. Write a for loop that prints each movie along with its position in the list (e.g., "1. Inception").
x=['Endgame', 'Infinity War', 'Avatar', 'Titanic', 'Inception']
count=0
for i in x:
    count+=1
    print(f"{count}.{ i}")

#3. Given a list of strings representing decimal numbers (e.g., ['1.1', '2.2', '3.3']), write a for loop that converts each string to a float, doubles the value, and prints the result.
str=['1.1','2.2', '3.3']
float_numbers=[]
for i in str:
    flt=float(i)
    float_numbers.append(flt*2)
print(float_numbers)

#4. Create a list of numbers from 1 to 20. Write a for loop that iterates through the list, converts each number to a string, and creates a new list with these string values. Print the new list.
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
string=[]
for i in numbers:
    string.append(str(i))
print(string)

#5. ⁠WAP that asks 10 user with their name and store them in a list. Print the name of only those users whose name starts with ‘a’ or ‘A’

User_name=[]
for i in range(10):
    name=input("Enter the Name: ")
    User_name.append(name)
for i in User_name:
    if(i[0]=='A' or i[0]=='a'):
        print(i)
 

#6. ⁠WAP that asks 10 user with their name and store them in a list. Print the name of only those users whose name ends with ‘a’ or ‘A’

User_name=[]
for i in range(10):
    name=input("Enter the Name: ")
    User_name.append(name)
for i in User_name:
    if(i[-1]=='A' or i[-1]=='a'):
        print(i)