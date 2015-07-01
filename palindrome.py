#iterative function to decide if palindromes
def iterate_palindrome(myuser, userbackwards):
    '''This function decides whether the two string inputs are palindromes iteratively'''
    mybool = False
    if myuser == userbackwards:
        mybool = True
    else:
        mybool = False
    return mybool

#recursive function to decide if palindromes
def recursive_palindrome(myuser, myuserindex, userbackwards, backwards_index):
    '''This function decides whether the two string inputs are palindromes recursively'''
    tempmyuserindex = myuserindex
    tempbackwards_index = backwards_index
    equalsofar = False
    if (myuserindex != len(myuser) - 1):
        myuserindex += 1
        if (myuser[tempmyuserindex] == userbackwards[tempbackwards_index]):
            tempmyuserindex += 1
            tempbackwards_index -= 1
            equalsofar = True
            recursive_palindrome(myuser, tempmyuserindex, userbackwards, tempbackwards_index)
        else:
            equalsofar = False
    return equalsofar

#get some user input
user_input = input("Please enter some text: ")

#change user input to all lowercase
user_input = user_input.lower()
print("The user input in lower case is: {}".format(user_input))

#change string into list where separated by spaces
user_input = user_input.split(' ')
print("The user input split where spaces exist is: {}".format(user_input))

#strip all punctuation out of string
count = len(user_input)
temp = 0
while temp <= count - 1:
    user_input[temp] = user_input[temp].strip(",<.>?;:-_=+~!")
    temp += 1
print("The user input after stripping each sub-string is: {}".format(user_input))

#turn list back into a string
user_input_temp = ""  #make new string variable in order to do the string join below
user_input_temp = user_input_temp.join(user_input)
print("The user input after changing it back to a string is: {}".format(user_input_temp))

#turn string backwards
user_input_backwards = ""
user_input_backwards = user_input_temp[len(user_input_temp) - 1::-1]
print("The user input backwards is: {}".format(user_input_backwards))

#call iterate palindrome function
if iterate_palindrome(user_input_temp, user_input_backwards) == True:
    print("is a palindrome")
else:
    print("is not a palindrome")

userindex = 0 #index for original input
backindex = len(user_input_backwards) - 1 #index for backwards input
#call recursive palindrome function
if recursive_palindrome(user_input_temp, userindex, user_input_backwards, backindex) == True:
    print("is a palindrome")
else:
    print("is not a palindrome")
