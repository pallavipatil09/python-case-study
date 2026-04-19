print("Question No.1")
# WAP to print the first and last character of all the names in the given list
l = ['Mayank', 'Aniket', 'Saurabh', 'Rahul']
'''
Expected output:
M k
A t
S h
R l
'''
for name in l:
    print(name[0],name[-1])

print("\nQuestion No.2")
# Write a Python program that takes two inputs from the user:
'''
An integer n representing the number of whole numbers (starting from 0).
An integer p representing the power to which each whole number should be raised.
The program should print the powers of the first n whole numbers.
Example Input:
Enter the value of n: 5
Enter the value of p: 2
Example Output:
0^2 = 0
1^2 = 1
2^2 = 4
3^2 = 9
4^2 = 16
5^2 = 25
'''

n = int(input("Enter the value of n:"))
p = int(input("Enter the value of p:"))

for i in range(n + 1):
    print(i,"^",p,"=",i ** p)

print("\nQuestion No.3")
# WAP to print the data type of each element in the given tuple.
t = ('Someone', 34, 'hi', 12.983, 34 +9j)
'''
Expected Output:
Someone, Type: <class ‘str’>
34, Type: <class ‘int’>
hi, Type: <class ‘str’>
12.983, Type: <class ‘float’>
(34+9j), Type: <class ‘complex’>
'''

for i in t:
    print(i,type(i))

print("\nQuestion No.4")
# WAP to print all the two digit even numbers which are also a multiple of 3.
'''
Expected Output:
12 18 24 30 36 42 48 54 60 66 72 78 84 90 96
'''

for i in range(100):
    if len(str(i)) == 2 and i % 2 == 0 and i % 3 == 0:
        print(i ,end = " ")

print("\nQuestion No.5")
# WAP to print the sum of individual tuples separately.

marksList = [(23, 24, 31), (56, 34, 53), (42, 58, 31)]
'''
Expected Output:
Sum of (23, 24, 31) = 78
Sum of (56, 34, 53) = 143
Sum of (42, 58, 31) = 131
'''
for marks in marksList:
    print("sum of",marks,"=",marks[0]+marks[1]+marks[2])

print()
#Using function
marksList = [(23, 24, 31), (56, 34, 53), (42, 58, 31)]
for marks in marksList:
    print("Sum of", marks, "=", sum(marks))

print("\nQuestion No.6")
# Write a Python program to print all numbers between 30 and 300 that are multiples of both 2 and 7.
'''
Expected output:
42 56 70 84 98 112 126 140 154 168 182 196 210 224 238 252 266 280 294
'''
for i in range(30,301):
    if i % 2 == 0 and i % 7 == 0:
        print(i,end = " ")

print("\nQuestion No.7")
# WAP to print even or odd for all the numbers in the given tuple.
t = (23, 45, 67, 90, 12, 10)
'''
Expected Output:
23 - Odd
45 - Odd
67 - Odd
90 - Even
12 - Even
10 - Even
'''
for i in t:
    if i % 2 == 0:
        print(i,"-","Even")
    else:
        print(i,"-","Odd")

print("\nQuestion No.8")
#Write a Python program that takes a string input from the user and reverses it.
'''
Note: Don't use slicing
Example Input: Enter a string: Python
Expected Output: Reversed string: nohtyP
'''
Text = input("Enter a string: ")
rev = ""

for i in range(len(Text)-1,-1,-1):
    rev = rev +Text[i]
print("Reversed string:",rev)


print("\nQuestion No.9")
# WAP to print the 2nd digit of all the numbers from this given collection.
t = (23, 45, 67, 90, 12, 10)
'''
Note: If a number has only one digit, print "No second digit".
Expected Output:
23 → 3
45 → 5
67 → 7
90 → 0
12 → 2
10 → 0
'''
for i in t:
    if len(str(i)) == 2:
        print(i,"->",str(i)[-1])
    else:
        print("No second digit")

print("\nQuestion No.10")
# WAP to print all the numerical data from the given list.
l = [2, 5, 'a', 5, 'r', 7, 'm', 't', '4']
'''
Expected Output:
2
5
5
7
4
'''
for i in l:
    if type(i) == int or i.isdigit():
        print(i)

print("\nQuestion No.11")
# WAP in Python to calculate the sum of all numbers from 1 to n.
'''
Take n as input from the user.
Example Input: Enter the value of n: 5
Example Output: Sum of numbers from 1 to 5 = 15
'''
n = int(input("Enter the value of n: "))
count = 0
for i in range(1,n+1):
    count += i
print("Sum of numbers from 1 to",n,"=",count)

print("\nQuestion No.12")
# Write a Python program that takes a number as input from the user and counts the total number of digits in the number.
'''

Example Input: Enter a number: 78645
Example Output: Total number of digits: 5
'''
number = int(input("Enter a number:"))
count = 0
while number > 0:
    number = number // 10
    count += 1
print("Total number of digits:",count)

print("\nQuestion No.13")
# Write a Python program that takes a number as input from the user and calculates its factorial.
'''
(Factorial of n is the product of all positive integers from 1 to n, denoted as n!.)
Example Input: Enter a number: 5
Example Output: Factorial of 5 is 120
'''
n = int(input("Enter a number: "))
factorial = 1
for i in range(1,n+1):
    factorial *= i
print(f"\nFactorial of {i} is {factorial}\n")

print("\nQuestion No.14")
# Print the following pattern using a loop.
'''
Take the number of rows as input from the user.
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
Example Input 1: Enter the number of rows: 5
Example Output 1:
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
Example Input 2: Enter the number of rows: 3
Example Output 2:
3 2 1
2 1
1
'''
no_of_rows = int(input("Enter the number of rows: "))
for i in range(no_of_rows,0,-1):
    for j in range(i,0,-1):
        print(j,end = " ")
    print()

no_of_rows = int(input("Enter the number of rows: "))
for i in range(no_of_rows,0,-1):
    for j in range(i,0,-1):
        print(j,end = " ")
    print()

print("\nQuestion No.15")
# WAP in Python to print only the string datatype from the given list

a = ['Samarth', 'Kunal', 'Jatin', 12, 75.5]

for i in a:
    if type(i) == str:
        print(i)

print("\nQuestion No.16")
# WAP in Python to check whether an input number is a Armstrong number or not.
'''
An Armstrong number is a number that is equal to the sum of its digits, each raised to the
power of the number of digits in the number.
For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
Single-digit numbers: All single-digit numbers (0-9) are Armstrong numbers.
Three-digit numbers: 153, 370, 371, and 407 are three-digit Armstrong numbers.
Four-digit numbers: 1634, 8208, and 9474 are four-digit Armstrong numbers.
'''
num = int(input("Enter a number:"))
temp = num
total = 0
digits = len(str(temp))

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10
if total == num:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")

print("\nQuestion No.17")
# WAP in python to print the sum of only those keys from the dictionary for which the value is NOT a square of the keys
d = {5:16, 3:9, 10:81, 1:0, 6:36}   

total = 0
for key,value in d.items():
    if value != key ** 2:
        total += key
print("sum:",total)

print("\nQuestion No.18")
# WAP to take a number as input from the user and print the sum of its’ digits.
num = int(input("Enter a number:"))
total = 0
while num >0:
    digit = num % 10
    total = total + digit
    num = num // 10
print("sum:",total)


print("\nQuestion No.19")
# WAP in Python to print the common elements between the given two lists.
'''
Maintain the order of the elements
'''
li1 =[10, 20, 50, 80, 60]
li2 = [50, 88, 95, 76, 81, 10, 60, 50, 60]

for i in li1:
    if i in li2:
        print(i)

print("\nQuestion No.20")
# WAP in Python to calculate the average of the marks for each student and print it.
d = {"Samarth": [45, 60, 50, 70], "Jati": [90, 95, 93, 91, 90], "Nishant":[93, 99, 98, 97, 91]}

for name ,marks in d.items():
    average_marks = sum(marks)/len(marks)
    print(name,"average marks:",average_marks)

print("\nQuestion No.21")
# WAP to search if a particular student name/rollno is present in the list or not. Take name/rollno as input and print the corresponding data.
'''
For e.g.
If user enters 4, print Harsh
If user enters Kunal, print 11
If user enters Mayank, print “Does not Exist”
'''
Name = ["Samarth", "Jatin", "Nishant", "Harsh", "Dabru", "Kunal"]
Roll_no = [1, 20, 13, 4, 9, 11]

data =input("Enter Name or Roll No:")
if data.isdigit():
    data = int(data)
    if data in Roll_no:
        index = Roll_no.index(data)
        print(f"\nYou entered Roll no which belongs to {Name[index]}\n")
    else:
        print("Does'nt exist")

else:
    if data in Name:
        index = Name.index(data)
        print(f"\nYou entered name which belongs to Roll No : {Roll_no[index]}\n")
    else:
        print("Does'nt exist")


print("\nQuestion No.22")
# WAP to print the digits of an input number in word format.
'''
i/p: Enter any number 85200
o/p:
Eight
Five
Two
Zero
Zero
'''

num =input("Enter a number:")
words = {"0":"Zero","1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine"}
for i in num:
    print(words[i])


print("\nQuestion No.23")
# WAP to create a fibonacci sequence of n digits. Take n as input.
n = int(input("Enter how many terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print("\nQuestion No.24")
# WAP to convert a decimal number to binary number.
'''
For e.g. i/p = 10
o/p = 1010
'''
num = int(input("Enter decimal number: "))
binary = ""

while num > 0:
    rem = num % 2
    binary = str(rem) + binary
    num = num // 2

print("Binary =", binary)

#using function
num = int(input("Enter decimal number: "))
print(bin(num)[2:])         # [2:] - Removes first two characters (0b) means binary prefix.

print("\nQuestion No.25")
# WAP to print all prime numbers between two input numbers using while loops.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

for n in range(num1, num2 + 1):
    a = True

    for i in range(2, n):
        if n % i == 0:
            a = False
            break

    if a and n > 1:
        print(n)

print("\nQuestion No.26")
# WAP in Python to check whether two strings are anagrams of each other using only for loops.
'''
Input: “listen”, “silent”
Output: True
An anagram of a string is another string that contains the same characters, only the order of
characters can be different.
'''
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print(False)

else:
    result = True

    for ch in s1:
        count1 = 0
        count2 = 0

        for i in s1:
            if i == ch:
                count1 += 1

        for j in s2:
            if j == ch:
                count2 += 1

        if count1 != count2:
            result = False
            break

    print(result)

#using method
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print(True)
else:
    print(False)

print("\nQuestion No.27")
# WAP to flatten a nested list (i.e., a list of lists) into a single list using for loops.
'''
Input: a = [[1,2], [3,4,5],[6]]
Output: 1, 2, 3, 4, 5, 6,
'''
a = [[1, 2], [3, 4, 5], [6]]

flat_list = []

for sublist in a:
    for item in sublist:
        flat_list.append(item)

print(flat_list)

print("\nQuestion No.28")
# WAP to calculate the sum of the product of corresponding elements from two lists.
'''
Input: a = [1, 2, 3], b = [4, 5, 6,]
Output: 32
Logic: (1*4 + 2*5 + 3*6)
'''
a = [1, 2, 3]
b = [4, 5, 6]

total = 0

for i in range(len(a)):
    total = total + (a[i] * b[i])

print(total)

print("\nQuestion No.29")
# WAP to print all possible pairs of elements from a list using nested for loops.
'''
Input: a = [1, 2, 3]
Output: 1, 1 \n 1, 2 \n 1, 3 \n 2, 1 \n 2, 2 \n 2, 3 \n 3, 1 \n 3, 2 \n 3, 3
'''
a = [1, 2, 3]

for i in a:
    for j in a:
        print(i, j)

print("\nQuestion No.30")
# WAP to create a list of the cumulative sum of elements of a given list using for loops.
'''
Input: a = [1, 2, 3, 4]
Output: [1, 3, 6, 10]
Cumulative sum means: Keep adding numbers one by one.
'''
a = [1, 2, 3, 4]

result = []
total = 0

for i in a:
    total = total + i
    result.append(total)

print(result)

print("\nQuestion No.31")
# WAP to print all the factors of a given input number.
'''
Input: n = 27
Output: Factors = 1, 3, 9, 27
'''
n = int(input("Enter a number: "))

print("Factors = ", end="")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")

print("\nQuestion No.32")
# WAP in Python to print the average of marks of each student only if the average is more than 90.
'''
Input:
d = {“Samarth”:[45, 60, 50, 90, 70], “Jatin”: [90, 95, 93, 91, 90], “Nishant”:[93, 99, 98, 97, 91]}
Output: Jatin Average is 91.8
Nishant Average is 95.6
'''
d = {
    "Samarth": [45, 60, 50, 90, 70],
    "Jatin": [90, 95, 93, 91, 90],
    "Nishant": [93, 99, 98, 97, 91]
}

for name, marks in d.items():
    avg = sum(marks) / len(marks)

    if avg > 90:
        print(name, "Average is", avg)

print("\nQuestion No.33")
# WAP to count the number of distinct elements in a list without using sets.
'''
Input: a = [1, 2, 2, 3, 4, 4, 5]
Output: 5
'''
a = [1, 2, 2, 3, 4, 4, 5]
count = []

for i in a:
    if i not in count:
        count.append(i)

print(len(count))

print("\nQuestion No.34")
# WAP to implement a Caesar Cipher encryption using a for loop, where n represents the number of shifts for each letter in the alphabet.
'''
Input: string = ‘hello, n = 3
Output: “Khoor”
Logic: Each alphabet is shifted by 3 positions.
'''
text = input("Enter text: ")
n = int(input("Enter shift: "))

for ch in text:
    print(chr(ord(ch) + n), end="")