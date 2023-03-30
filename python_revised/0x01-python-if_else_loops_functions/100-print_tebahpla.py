"""
*loop through the lowercase alphabets in reverse order
*find the odd numbers
*change the odd position to uppercase
*print the final loop using string format
"""
for i in range(122, 96, -1):
    if i % 2 != 0:
        i = i - 32
    print("{}".format(chr(i)), end='')
