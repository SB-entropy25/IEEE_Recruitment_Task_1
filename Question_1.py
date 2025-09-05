n = int(input("Enter the value of n:")) #we take input from user regarding value of number of rows
for i in range(1, n+1):        #in 1st line there are n-1 blanks and correspondingly in i th line there are n-i blanks before i *s
    print(' ' * (n-i) + '*' * i)


