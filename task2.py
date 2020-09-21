# Check whether the input string is palindrome.
palindrome = input("input palindrome\n")
# Removes all case distinctions
palindrome = palindrome.casefold()
rev_palindrome = reversed(palindrome)
if list(palindrome) == list(rev_palindrome):
    print("yes")
else:
    print("no")