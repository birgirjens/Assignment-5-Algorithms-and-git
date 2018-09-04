n =  int(input("Enter the length of the sequence: ")) # Do not change this line
#initializing values for the formula
n1 = 0
n2 = 1
n3 = 2

for i in range(n):
    seq = n1 + n2 + n3 #The sum of the 3 numbers in the sequence
    n1 = n2            #Moving the values around to continue with the sequence    
    n2 = n3            #Moving the values around to continue with the sequence
    n3 = seq           #n3 now has the value of the next number in the sequence
    print(n1)          #Here the sequence is printed
                       #All the other variables will give the same sequence but will not satisfy the test
                       #So in order to satisfy the test, n1 must be printed