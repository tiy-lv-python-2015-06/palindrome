#Write a program that asks the user for one or more sentences and
#then lets the user know if it is a palindrome.
import re

#functions are self-sustaining code and shouldn't rely on anything outside
#of themselves to do what they're supposed to do except what
#arguments are passed to them
def raw_sentence():
    """Returns exact user input"""
    return input("\nGive me a sentence and I will tell you if it is a palindrome \n >" )

def strip_sentence():
    """Gets user sentence, returns without spaces and punctuation"""
    #sentence = input("\nGive me a sentence and I will tell you if it is a palindrome " )
    return re.sub(r'[^A-Za-z]', "", raw_sentence().lower())

#print(strip_sentence())
#stripped_sentence = strip_sentence()
#print("first letter:")
#print(stripped_sentence[0])
#print("last letter:")
#print(stripped_sentence[-1])

def overall_loop():
    counter = (len(stripped_sentence))-1
    index = 1
    palindrome(counter, index)

def palindrome(counter, index):
    """Given length of stripped_sentence checks to see if palindrome"""
    if counter > 0:
        if stripped_sentence[index] != stripped_sentence[-(index+1)]:
            print("That is not a palindrome")
        else:
        #stripped_sentence[index] == stripped_sentence[-(index+1)]:
            palindrome(counter-1, index+1)
            print(index)
            print(stripped_sentence[-(index+1)])
            print(stripped_sentence[(index)])
            print("That is a palindrome")

stripped_sentence = strip_sentence()
overall_loop()
