max_int = 0
num_int = 0

while(num_int>=0): #Loops through until num_int is a negative number (>0)
    num_int = int(input("Input a number: "))    # Do not change this line #ok I won't
    if num_int > max_int: #comparing num_int to the current value of max_int
        max_int = num_int #giving max_int the value of num_int if num_int is larger then the current value of max_int

print("The maximum is", max_int)    # Do not change this line #ok I won't
