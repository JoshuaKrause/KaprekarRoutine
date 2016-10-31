'''
Kaprekar by Joshua Krause (jkrause@joshuakrause.net)

Returns the number of iterations in Kaprekar's Routine, which is as follows:

Given a 4-digit number that has at least two different digits, take that number's descending digits, and subtract that number's ascending digits. For example, given 6589, you should take 9865 - 5689, which is 4176. Repeat this process with 4176 and you'll get 7641 - 1467, which is 6174.
Once you get to 6174 you'll stay there if you repeat the process. In this case we applied the process 2 times before reaching 6174, so our output for 6589 is 2.

Done as an exercise from reddit.com/r/dailyprogrammer/.
'''


# Helper function that converts a four-digit integer into a sorted list.
# If the list is less than four digits, pad it with zeros.
def sort_digit(digit, reverse = False):
    a = list(str(digit))
    while len(a) < 4:
        a.insert(0, '0')
    a.sort(reverse=reverse)
    return a

# Helper function that checks the length of an integer and 
# ensures that it contains at least two different digits.
def check_digits(digit):
    if len(list(str(digit))) < 4 or all(x == list(str(digit))[0] for x in list(str(digit))):
        return False
    else:
        return True

# Returns the largest digit in an integer.    
def largest_digit(digit):
    return int(sort_digit(digit, True)[0])

# Returns an integer as its ascending digits.
def asc_digits(digit):
    return int(''.join(sort_digit(digit, False)))

# Returns an integer as its descending digits.
def desc_digits(digit):
    return int(''.join(sort_digit(digit, True)))

# Returns the Kaprekar count of a four-digit integer.
def kaprekar(digit):
    # If the digit is 6174, return.
    if digit == 6174:
        return 0
    # Check to ensure that the digit is valid (ie a four-digit integer containing two different digits.
    elif not check_digits(digit):
        return 'Invalid digit.'
    else:
        a = asc_digits(digit)
        d = desc_digits(digit)
        result = 0
        count = 0
        # Loop through until the result is 6174. Return the number of loops.
        while result != 6174:
            result = d - a
            a = asc_digits(result)
            d = desc_digits(result)
            count += 1
        return count

# Finds the four digit integer with the highest Kaprekar count
def find_best_kaprekar():
    i = 1000
    best_number = 0
    best_count = 0
    while i <= 9999:
        if check_digits(i):
            if kaprekar(i) > best_count:
                best_number = i
                best_count = kaprekar(i)
        i += 1
    return best_number, best_count


print kaprekar(6589)
print kaprekar(1111)
print kaprekar(6174)
