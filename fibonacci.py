n = int(input("Enter how many number you want from fibonacci series" "\t: "))
first_num = 0
second_num = 1

for i in range(n):
    print(first_num)
    temp = first_num
    first_num = second_num
    second_num = temp+first_num


##created a temp variable to store first number
