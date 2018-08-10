#1 - Write a program which should return the list on a single line containing the cubes of the first
#6 Fibonacci numbers. HINT: Use Lambda function.

fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
cube_fib = map(lambda x: x**3, fib(6))


#2 - Write a program to take input from the user in following formats and also check their type by
#using type function.
#Formats: Integer, Float, String & Complex

x = int(raw_input('Please enter some integer input'))
type(x)

y = float(raw_input('Please enter a float input'))
type(y)

s = str(raw_input('Please enter a string value'))
type(s)

c = complex(raw_input('Please enter a complex number')) 
type(c)

#3 - Write a program for the following conditions:
#- If a user enters a negative number it should break the loop
#- If a user enters any positive value it will run the loop for infinite.

while True:
	x =int(raw_input('Please enter a integer'))
	if x < 0:
		break


#4 - Write a program to multiply the first 10 even integer number starting from 1 & store them in
#result variable.

p = reduce((lambda x, y: x*y), list(filter(lambda x: x%2 ==0, range(1,21))))


#5 - Write a program to concatenate the string of those characters which exist at the even
#position in "innovationwithpython".

emp_lis = ' '
a =  'innovationwithpython'
for i in range(len(a)):
	if i%2 == 0:
		emp_lis = emp_lis + a[i]

#6 - Write a function to return the list of those numbers in a range of 1 to 50 which is a multiple
#of 2 and 6 both. Also, calculate the sum of last three values.

def mul_2_6():
	emp_lis = []
	for i in range(1,50):
		if i%2 == 0 and i%6 == 0:
			emp_lis.append(i)
	print emp_lis
	return sum(emp_lis[-3:])


#7 - Write the higher order function reduce to calculate the total sum of first 30 odd values in he
range of 1 to 100.

al = list(filter(lambda x: x%2, range(1,100)))
s = reduce(lambda x, y: x+y, al[0:31])

#8 - What will be the output of the following:
#new_list=[ 1 , 2 , 3 , 4 , 5 , 6 , [ "Riyaz" , "Ul" , "Haque" , 7 ] , 8 , 9 , 10 ]
#--- new_list [ -4 ] ---> [ "Riyaz" , "Ul" , "Haque" , 7 ]
#--- new_list [ 4 ] ---> 5
#--- new_list [ 6 ] [ 1 ] ---> 'Ul'
#--- new_list . append ( [ "new" ] ) ---> [ 1 , 2 , 3 , 4 , 5 , 6 , [ "Riyaz" , "Ul" , "Haque" , 7 ] , 8 , 9 , 10 ,['new']]
#--- new_list . sort( ) --->  [1, 2, 3, 4, 5, 6, 8, 9, 10, ['Riyaz', 'Ul', 'Haque', 7], ['new']]

#9 - Write a function that takes three arguments which after concatenation should print
#"innovationwithpython" . This is a void type function.

def print_fn(a,b,c):
	print a+b+c

print_fn('innovation','with','python')
	
	
#10 - What is :
#--- Negative indexing in python ---> When we access a data structure from the last index is called negative indexing
#--- Packing and UnPacking  --------> Packing is when we do not know the number of arguments needed to be passed to the function, 
#										we use packing to pack all arguments in a tuple
#										Syntax is *args  

#									Similarly, unpacking is when we have to pass multiple arguments in a function and we have a list of length equivalent to 
#									number of arguments required for function.  


									
#--- Mutable and Immutable ---------> Mutable data types in python are which can be changed and immutable cannot be changed

#--- Append and Extend  ------------> Append is to add elements to a list, it increases the size of list by 1, if we pass multiple elements using append
#									function, all functions will be added to the next index as a list
#									Extend is used to extend the list to the number of index equivalent to number of elements passed
#--- Pickling and Unpickling

#11 - Write a function that should multiple three entered values. Now use this function in the
#different module and take three values as 11, 12 & 13. HINT: Use import

def mul(a, b, c):

	res = a*b*c

import mul

#12 - write a program to generate a dictionary that contains ( i , i * i ) such that is an integral
#number between 1 and n (both included). and then the program should print the dictionary.
#Suppose the following input is supplied to the program:
#4
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16}

def gen_dict():
	n = int(raw_input('Enter the length of the dictionary'))
	dict = {i: i*i for i in range(1, n+1)}
	print(dict)

#13 - What is split function in python?

#Python split function is used to break the string into smaller chunks, the syntax for split function is var.split(), where var is a string variable.
#e.g- a = "This is a string", if we apply the split function on this string it will gennerate this output.
#a.split() ----> ['This', 'is', 'a', 'string']

#By default, the split function breaks the string where the spaces are present in the string. We can pass the character that we want to used as the split function
#e.g.- a = "This is a string"
#a.split('i') ----> ['Th',  's ', 's a str', 'ng']

#14 - Write a program which accepts a sequence of comma-separated numbers from the
#console and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

n = raw_input('Enter a sequence of comma-seperated values')
a = n.split(',')
print (a)

b = tuple(a)
print (b)


#15 - Write a program which accepts a string from console and prints it in reverse order.

def rev_str(a_string):
	return a_string[::-1]

#16 - Find out the common character from the two different string using set.

string_A = 'Hello my name is Sahil'
string_B = 'Hello your name is ???'
set(string_A) & set(string_B)


#17 - Write a program that read the sentence and gives the output as the length of each word in
#a sentence in the form of a list.

s = 'This is the string we want to find length of each word'
map(len, s.split())

#18 - Write a program to concatenate the following dictionaries to create a new one.
#Sample Dictionary:
#dic1= {1:’a’, 2:’b’}
#dic2= {3:’c’, 4:’d’}
#dic3= {5:’e’, 6:’f’}
#Expected Result: {1: ‘a’, 2: ‘b’, 3: ‘c’, 4: ‘d’, 5:’e’ , 6: ‘f’}

#Python 3 solution 
updated_dict = {**dic1, **dic2, **dic3}


#19 - What is memory Management in Python?


# 20 - What is the difference between range and xrange function
#Range function returrns list of numbers passed inside the range() function while xrange() returns the range object
