import re

def input_sentence():
    '''Asks for sentence, then returns that sentence without case or punctuation'''
    return re.sub(r'[^A-Za-z0-9]','', input("What is your sentence?\n").lower())

def is_palindrome(test_sentence, count):
    '''Takes a sentence (stripped of case and punctuation) and recursivly checks if it is a palindrome'''
    if count < len(test_sentence)/2:
        if test_sentence[count] == test_sentence[-(count + 1)]:
            print('Checking the {} and {} letters of the string'.format(count, (-(count+1))))
            count += 1
            is_palindrome(test_sentence, count)

        else:
            print('is not a palindrome')
    else:
        print("is a palindrome")

is_palindrome(input_sentence(), 0)
