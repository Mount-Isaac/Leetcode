# Level Medium
def reverse(x):
    """
    Given a signed 32-bit integer x, 
    return x with its digits reversed. 
    If reversing x causes the value to 
    go outside the signed 32-bit integer 
    range [-231, 231 - 1], then return 0.
    """
    if x == 0:
        return 0
    
    def check_integer(x):
        x = int(x)
        if not -2**31 <= x <= 2**31-1:
            return str(0)
        else:
            return str(x)

    # convert the int to a string
    x_str = str(x)

    # function to reverse 
    def reverse_integer(x):
        return x[::-1]
    
    # conversion testcases
    if x_str[0] == '-':
        check_str = check_integer(reverse(x_str[1:]))
        if check_str == '0':
            return 0
        return int('-' + x_str)
    
    elif x_str[-1] == '0':
        check_str = check_integer(reverse(x_str[:-1]))

        if check_str == '0':
            return 0
        return int(check_str)
    else:
        return int(check_integer(reverse_integer(x_str)))


