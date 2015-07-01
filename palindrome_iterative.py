import re

def input_sentence():
    '''Asks for sentence and returns that sentence without case or punctuation'''
    return re.sub(r'[^A-Za-z0-9]','', input("What is your sentence?\n").lower())

def check_palindrom(test_sentence):
    '''Recieves a sentence (strippped of case and punctuation) and determines if it is a plaindrome'''
    if test_sentence[:] == test_sentence[::-1]:
        print('is a palindrome')
    else:
        print('is not a palindrome')

check_palindrom(input_sentence())
