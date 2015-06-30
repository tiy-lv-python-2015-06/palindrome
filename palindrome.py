# Write a program that asks the user for one or
# more sentences and then lets the user know if it is a palindrome.

import re

def remove_punctuation(this_string):
    """ The function will remove spaces and punctuation (basically anything
        other than a-z) from our
        test string since we do not want to include those characters
        in the test and return the string
    """
    # take out spaces and punctuation
    my_new_string = re.sub(r'[^a-z]', "", this_string)

    return my_new_string


def is_a_palindrome_it(this_string):
    """ This function will test the string to see if it is a palindrome iteratively - if
        it is it will return true, if it is not it will return false
    """
    r_value = False

    forward_string = this_string[::1]
    backward_string = this_string[::-1]

    if forward_string == backward_string:
        r_value = True

    return r_value


def is_a_palindrome_rec(this_string):
    """ This function will test the string to see if it is a palindrome recursively - if
        it is it will return true, if it is not it will return false
    """

    result = True

    end = len(this_string) - 1
    if end >= 1:
        if this_string[0] == this_string[end]:
            sub_string = this_string[1:end-1]
            is_a_palindrome_rec(sub_string)
        else:
            result =  False

    return result


# ask the user for the string to test - immediately convert to lower case
user_string = input("Please enter some text here....").lower()

# lets remove the punctuation as we are not including it in the test
test_string = remove_punctuation(user_string)

# ok now lets test if this is a palindrome
if (is_a_palindrome_rec(test_string) and is_a_palindrome_it(test_string)):
    print("is a palindrome")
else:
    print("is not a palindrome")
