def myAtoi(s):
    def evaluate_sign(s):
        '''
        Tn O(n)
        handle all the signs testcases
        '''
        for index in range(len(s)):
            try:
                if s[index] == "-":
                    if s[index+1] == "+":
                        return str(s)
                    if s[index+1] == "-":
                        return str(s)
                if s[index] == "+":
                    if s[index+1] == "+":
                        return str(s)
                    if s[index+1] == "-":
                        return str(s)
            except:
                return s
        return s
    # new string after removing leading whitespaces 
    s = ''.join(evaluate_sign(s.strip(' ')).split(".")[0])

    def check_limit(s):
        '''
        Tn O(n-1)
        Check if the string is a 32bit signed integer
        '''
        if -2**31 <= s  <= 2**31-1:
            return s
        else:
            if s < -2**31:
                return -2**31
            return 2**31-1

    if len(s) == 0:
        return 0
    if len(s) == 1 and s.isnumeric():
        return int(s)
    if len(s) == 1 and not s.isnumeric():
        return 0
    
    if s[0] == '-':
        for index in range(1,len(s)):
            if not s[index].isnumeric():
                if not len(s[:index]):
                    return 0
                elif index == 1:
                    return 0
                return check_limit(int(s[:index]))
        return check_limit(int(s))
    elif s[0] == '+':
        for index in range(1,len(s)):
            if not s[index].isnumeric():
                if not len(s[:index]):
                    return 0
                elif index == 1:
                    return 0
                return check_limit(int(s[:index]))
        return check_limit(int(s))
    else:
        for index in range(len(s)):
            if not s[index].isnumeric():
                if not len(s[:index]):
                    return 0
                elif index == 1 and not s[index-1].isnumeric():
                    return 0
                return check_limit(int(s[:index]))
        return check_limit(int(s))

