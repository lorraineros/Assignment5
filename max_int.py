num_int = int(input("Input a number: "))    # Do not change this line

max_int=0
while num_int:
    number=int(input("Input a number: "))
    if number < 0:
        break
    if number > max_int:
        max_int = number

print("The maximum is", max_int)    # Do not change this line
