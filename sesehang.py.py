#Create a list of the first 10 positive integers. Write a for loop that calculates and prints the sum of all numbers in the list.
x = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in range(len(x)):
    sum += x[i]
    print(sum)

#Create a list of your five favorite movies. Write a for loop that prints each movie along with its position in the list (e.g., "1. Inception").
movies= ["3 idots","titanic","2012","jhola","interstellar"]
for i in range(len(movies)):
    print(f"{i+1}. {movies[i]}")


#Given a list of strings representing decimal numbers (e.g., ['1.1', '2.2', '3.3']), write a for loop that converts each string to a float, doubles the value, and prints the result.
num = ["2.5","4.5","5.5","3.33","9.9"]
for i in num:
    f_num = float(i)
    val = f_num*2
    print(val)



#Create a list of numbers from 1 to 20. Write a for loop that iterates through the list, converts each number to a string, and creates a new list with these string values. Print the new list.
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
strings = []
for i in num:
    convert = str(i)
    strings.append(convert)
print(strings)




#WAP that asks 10 user with their name and store them in a list. Print the name of only those users whose name starts with ‘a’ or ‘A’
n=[]
for i in range(10):
    x=input("enter your name: ")
    n.append(x)
print("the names that starts with 'a' or 'A':\n")
for i in n:
    if(i[0]=='a' or i[0]=='A'):
        print(i)



#⁠WAP that asks 10 user with their name and store them in a list. Print the name of only those users whose name ends with ‘a’ or ‘A’
std_name=[]
for i in range(10):
    y=input("enter your name: ")
    std_name.append(y)
print("the names that wnds with 'a' or 'A':\n")
for i in std_name:
    
    if(i[-1]=='a' or i[-1]=='A'):
       print(i)
