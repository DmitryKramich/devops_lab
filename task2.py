# check whether the input string is palindrome.
palindrome = input("input palindrome\n")
palindrome = palindrome.casefold()  # removes all case distinctions
rev_palindrome = reversed(palindrome)
if list(palindrome) == list(rev_palindrome):
    print("yes")
else:
    print("no")

