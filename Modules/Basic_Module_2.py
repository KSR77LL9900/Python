#IF-ELSE- 2.1
#a=int(input("Any integer value: "))
a=5
if(a>5):
    print("IF CONDITION IS WORKING")
else:
    print("ELSE CONDITION IS WORKING")

#WHILE LOOP- 2.2
#Loops are either infinite or conditional. Python while loop keeps reiterating a block of code defined inside it until the desired condition is met.
#The while loop contains a boolean expression and the code inside the loop is repeatedly executed as long as the boolean expression is true.
#The statements that are executed inside while can be a single line of code or a block of multiple statements.

i=1
while i<=6: 
    print(i) 
    i=i+1

count = 0 
while (count < 9): 
    print("The count is:", count) 
    count = count + 1 
    print("Good bye!")

#FOR LOOP
#Python for loop is used for repeated execution of a group of statements for the desired number of times. It iterates over the items of lists, tuples, strings, the dictionaries and other iterable objects.

numbers = [1, 2, 4, 6, 11, 20] 
for val in numbers: 
    seq=val*val 
    print(seq)

list = ['K','A','M','A','L'] 
i = 1
for item in list: 
    print ('NAME ',i,' is ',item) 
    i = i+1

for i in range(1,6): 
    for j in range(0,i): 
        print(i, end=",")
    print('')

for i in range(1,6): 
    for j in range(5,i-1,-1): 
        print(i, end=" ")
    print('')

# BREAK
#The break statement terminates the loop containing it and control of the program flows to the statement immediately after the body of the loop. If break statement is inside a nested loop (loop inside another loop), break will terminate the innermost loop.
for num in [11, 9, 88, 10, 90, 3, 19]: 
    print(num) 
    if(num==88): 
        print("The number 88 is found") 
        print("Terminating the loop") 
        break
for letter in "Python": # First Example 
    if letter == "h": 
        break
    print("Current Letter :", letter )

#CONTINUE
#The continue statement is used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.
for val in "string": 
    if val == "i": 
        continue
    print(val)
print("The end")

#PASS
#In Python programming, pass is a nullstatement. The difference betweena comment and pass statement in Python is that, while the interpreter ignores a comment entirely, pass is not ignored. pass is just a placeholder for functionality to be added later.
sequence = {'p', 'a', 's', 's'} 
for val in sequence: 
    pass