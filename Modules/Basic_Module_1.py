#INTRODUCTION TO PYTHON- 1.1
#Python is a high-level, interpreted programming language renowned for its simplicity and readability. Its emphasis on clear syntax makes it an excellent choice for both beginners and experienced programmers, and also known for his readability,Versatility, large community, Extensive libraries and Rapid Development.

#PRINT STATEMENT- 1.2
#Print function is used to  display the values on the console screen.By this we print multiple values at a time.
#print(age,name,address)
print("Hi! Welcome")

#ARITHMETIC OPERATORS- 1.3
#Arithmetic operators are used to perform mathematical operations on numerical values. Python supports several arithmetic operators like Addition(+), Substraction(-), Multiplication(*), Division(/), Modulus[returns the remainder of a division](%), Floor division[division that rounds down to the nearest integer](//), Exponentiation[raises a number to a power](**)
x=123
y=321
print(x+y,x-y,x*y,x/y,x%y,x//y,x**y)


#STRING VS OPERATIONS- 1.4
#String is used to store text, syntax is enclosed in quotes and data is immutable.
#Operations is used to perform actions, syntax uses operators and in this we can change the data.

#DIFFERENCE BETWEEN PYTHON AND C- 1.5
#Python is a High-level, interpreted, Readable, English-like, Slower due to interpretation, Automatic garbage collection, Object-oriented, procedural, functional, Data science, machine learning, web development, scripting.
#C is a Low-level, compiled, Complex, with curly braces and semicolons, Faster due to compilation, Manual memory management, Procedural, structured, System programming, embedded systems, performance-critical applications.

#ADDING COMMENTS- 1.6
#We can add comments in the code to remember the concepts or the logic that we used in the code.

#DEFINING A VARIABLE- 1.7
#We can define a variable by using equal_to_sign(=) like x=10, in this x is a variable.
abc=123

#TAKING INPUT- 1.8
#We can get input from the system by applying the input function like [input()]
print(int(input("ANY INTEGER: ")))

#CONVERT INPUT(string) TO AN Integer- 1.9
x=input("A Integer Containing String Changing into an Integer: ")
x=int(x)
print(x,"This is of",type(x))

#BATTING STRIKE RATE CALCULATOR
R=int(input("Enter the runs scored by the batsman: "))
B=int(input("Enter the number of balls faced by the batsman: "))
avg=((R/B)*100)
print(avg)