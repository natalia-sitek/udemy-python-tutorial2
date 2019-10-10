# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".


for liczba in range(0, 101):
    if liczba % 15 == 0:
        print("FizzBuzz")
    elif liczba % 5 == 0:
        print("Buzz")
    elif liczba % 3 == 0:
        print("Fizz")
    else:
        print(liczba)
