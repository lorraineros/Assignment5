n = int(input("Enter the length of the sequence: ")) # Do not change this line
nums=[]
answer=0
for i in range(1,n+1):
    if i < 3:
        print(i)
    else:
        i+=(i-1) + (i-2) + (i-3)
        print(i)