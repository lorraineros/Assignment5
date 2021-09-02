n = int(input("Enter the length of the sequence: ")) # Do not change this line
a = 0
b = 1
c = 2
for i in range(1,n+1):
    if i < 3:
        print(i)
    else:
        answer = a+b+c
        print(answer)
        a = b
        b = c
        c = answer