##c = 0
##for number in range(1, 5+1):
##    print(number)
##    c = c + number
##print(c)    


##def add_numbers():
##    c = 0
##    for number in range(1, 100 + 1):
##        print(number)
##        c = c + number
##    print(c)
##    return
##
##anwser = add_numbers()
##print(anwser)

 
def add_numbers(start,end):
    c = 0
    for number in range(start, end + 1):
        print(number)
        c = c + number
    print(c)
    return

test1 = add_numbers(1,2)
print(test1)

test3 = add_numbers(333,777)
