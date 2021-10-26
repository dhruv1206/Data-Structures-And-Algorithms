def reverse_string(input):
    if len(input)<=1:
        return input
    return reverse_string(input[1:])+input[0]

def is_palindrome(input):
    return input==reverse_string(input)

print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")
