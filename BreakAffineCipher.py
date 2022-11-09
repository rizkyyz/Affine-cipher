import math
# Using math module again for greatest common divider.
import time
# For testing purposes, i was monitoring efficient ways of running it.

array = (open("dictionary.txt").read()).split("\n")
# This line imports the dictionary file and reads it, splits each item by the new line
# And assigns each new line to the array as a seperate element, creating a big array with words to be used later.


def crackAffine(m):
    plainText = ''
    counter = 0
    matchList = []

    encryptText = input('Please enter your encrypted text: \n')
    encryptText = encryptText.upper()

    start_time = time.time()
    # Sets start time here (time.time() is the current time).

    length = len(encryptText)
    # Simular to decryption however only asks for the encrypted text, not the keys.

    print('Thank you, working on it...')

    coprimes = []
    for i in range(m):
        # A function which takes m, the range of letters, and checks for coprimes in that range.
        testI = math.gcd(int(i), int(m))
        if testI == 1:
            coprimes.append(i)
            # If it is a coprime, appends it to the end of the array.

    for i in range(len(coprimes)):
        # Nested for loops. This one takes the "a" variable, which needs to be the coprime, from the coprime array.
        a = int(inverse(coprimes[i], m))
        for b in range(m):
            # This loop takes the "b" variable, from 0 to "m".
            plainText = ''
            for y in range(length):
                # This one takes the letters from the encrypted text one by one as "y".
                encryptNum = ord(encryptText[y])
                # Changing it to Unicode number.
                if encryptNum >= 65 and encryptNum <= 90:
                    # If character was a capital letter, runs through this if loop.
                    plainNum = (((encryptNum - 65) - b) * a) % m
                    # This is the decryption algorithm, using "a", "b", "m" and the Unicode number of character.
                    plainText += chr(plainNum + 65)
                    # Appends the final character version of Unicode number to end of string.
                    counter += 1
                    # For testing.
                elif encryptNum == 32:
                    # If space, adds it to the string too
                    plainText += chr(encryptNum)
                    counter += 1
                # Every other character gets discarded.

            match = dictionaryCheck(plainText)
            # Assign the returned class object
            if match.weight != 0:
                # Check the weight value of class and goes into if statement if not 0.
                matchList.append(match)
                # Appends the instance of the class to matchList, which keeps all the possible ones which triggered

    sortedList = sorted(matchList, key=lambda i: i.weight, reverse=True)
    # Make a new list from matchList, which gets organised in descending order
    # Lambda is a anonymous function, it takes the weight value and organises by them.

    print("My program took", time.time() - start_time, "to run")
    # This is the end of timeing. If we go on for longer, the inputs make the time very extended
    # And not even neceserry after, as not many calculations, functions happening after this.

    for z in sortedList:
        print(z.text, "with a weight of", z.weight)
        # For loop goes through the sorted list from the one with highest weight, and prints them one by one.
        trigger = input(
            "Enter \"Exit\" if you found it, or press enter to continue or enter \"All\" for all results:\n")
        if trigger == "Exit":
            break
        elif trigger == "All":
            for x in sortedList:
                print(x.text, "with a weight of", x.weight)
                # Gives the option to see all the words which matched instead of going through them one by one.
            break


def inverse(a, m):
    a1 = 1
    a2 = a

    b1 = 0
    b2 = m

    while b2 != 0:
        # Loops around untill b2 is equal to 0 (so the remainder is 0).
        x = a2 // b2
        b1, b2, a1, a2 = (a1 - x * b1), (a2 - x * b2), b1, b2
        # All in one line so they all get changed at same time, and not messsed up by the new values.
    return a1 % m
    # Returns the remainder. This is to make sure it is not a negative number or a large number.


def dictionaryCheck(plain):
    # This function is used to compare the strings which go through brute force to the dictionary array.
    lenCounter = 0
    for i in array:
        # Takes each word from the array one by one
        if i in plain:
            # If the word is in the string
            lenCounter += len(i)*len(i)
            # Adds the number of letters squared to the counter

    class textCounter:
        # Made a class to contain the counter and text to be able to return to other function
        def __init__(self):
            # Init is a reserved method in classes, a constructor. Specify all the values in it by self.value
            self.text = plain
            self.weight = lenCounter

    return textCounter()
    # Return it to function.


def main():
    m = 26
    # Range of letters.
    crackAffine(m)
    # Starts the function with argument "m".
    # Encrypted text is "YFKLZOYWFFSRYGSC"

    trigger = input("Press enter to exit or type \"Again\" to restart.")
    if trigger == "Again":
        main()


main()
# Boots up the start of the program.
