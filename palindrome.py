#Write a program that asks the user for one or more sentences and
#then lets the user know if it is a palindrome.
import re

def raw_sentence():
    """Returns exact user input"""
    return input("\nGive me a sentence and I will tell you if it is a palindrome \n >" )


def strip_sentence(raw_sentence):
    """Gets user sentence, returns without spaces and punctuation"""
    stripped_sentence = re.sub(r'[^A-Za-z]', "", raw_sentence.lower())
    return stripped_sentence

def is_palindrome(stripped_sentence):
   if (stripped_sentence):
      if (stripped_sentence[0] == stripped_sentence[-1]):
         result = is_palindrome(stripped_sentence[1:-1])
         print(stripped_sentence[1:-1])
         print("is a palindrome")
         if result:
            return True
   else:
      return True
   return False

if __name__ == "__main__":
   answer = is_palindrome(strip_sentence(raw_sentence()))
   print("ANSWER:")
   if not answer:
        print("is not a palindrome")
   else:
        print("is a palindrome")