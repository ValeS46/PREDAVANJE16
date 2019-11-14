name = input("What is your name?")
print ("Wellcome "+ name + " to the program Guess the secret number! You can won 10.000$")

secret = 77

guess = int(input("Guess the secret number (from 1 to 100): "))

if guess == secret:
    print("Congratulations your number " + str(guess) + " is correct! You won 10.000$")
else:
    print("Too bad your input number " + str(guess) + " is not correct! You didn't won 10.000$")

print("Konec programa!")