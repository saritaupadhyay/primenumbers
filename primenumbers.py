def prime_number(input):
    input = int(input)
    if (input == 0):
        return False
    elif (abs(input)) ==1:
        return True
    else:
        for i in range (2,input):
            if input%i==0:
                return False
        return True


def main():
    while (True):
        input = raw_input("Type exit to exit. Enter a number: ")
        if input == "exit":
            break
        else:
            check = prime_number(input)
            if check ==True:
                print "Your number is prime."
            else:
                print "Your number is not prime."


main()





