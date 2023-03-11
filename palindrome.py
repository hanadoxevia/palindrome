def palindrome():
    try:
        number = int(input("Type in a number to find out if its a palindrom: "))
        number = int(number)
    except ValueError:
        print("Does this looks like a number to you?")
        return(palindrome())
    
    res = str(number) == str(number)[::-1]

    if res == True:
        print("Your number is a palindrome")
    elif res == False:
        print("Your number is no palindrome")
    else:
        print("Does this looks like a number to you?")
    palindrome()
palindrome()
