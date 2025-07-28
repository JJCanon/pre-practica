def fizzBuzz(n):
    lst=[]
    for number in range(1,n+1,1):
        if number%3 == 0 and number%5 == 0:
            lst.append('FizzBuzz')
        elif number%3 == 0:
            lst.append('Fizz')
        elif number%5 == 0:
            lst.append('Buzz')
        else:
            lst.append(number)
    return lst


print(fizzBuzz(15))