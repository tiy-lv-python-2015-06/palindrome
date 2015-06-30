#Write a program that asks the user for one or more sentences and
#then lets the user know if it is a palindrome.
import re

sentence = input("\nGive me a sentence and I will tell you if it is a palindrome" )

def strip_sentence():
    """Gets user sentence, returns without spaces and punctuation"""
    #sentence = input("\nGive me a sentence and I will tell you if it is a palindrome" )
    return re.sub(r'[^A-Za-z]', "", sentence.lower())

print(strip_sentence())

def test_pal(sentence):
    """Returns if palindrome given stripped sentence"""
    length = len(sentence)
    index = 0
    count = length / 2
    while count > 0
        if sentence[(0 + index)] == sentence[(index - 1)]:
            print("{} is a palindrome".format(sentence))
            
    #compare first index of the list to the last index of the list
    #if they are the same then compare the first+1 to the last-1
    #
    return is_palindrome
