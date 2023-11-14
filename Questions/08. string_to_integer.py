def myAtoi(s):
    s = s.replace(' ', '')

    def check_limit(s):
        if -2**31 <= s  <= 2**31-1:
            return s
        else:
            if s < -2**31:
                return -2**31
            return 2**31-1

    if len(s) == 0:
        return ""
    if len(s) == 1 and isinstance(s, int):
        return s
    if len(s) == 1 and not isinstance(s, int):
        return 0
    
    if s[0] == '-':
        for index in range(1,len(s)):
            # print('index', s[index])
            if not s[index].isnumeric():
                if not len(s[:index]):
                    return ''
                return check_limit(int(s[:index]))
        return check_limit(int(s))
    else:
        for index in range(len(s)):
            if not s[index].isnumeric():
                if not len(s[:index]):
                    return ''
                return check_limit(int(s[:index]))
        return check_limit(int(s))


print(myAtoi("-+12"))

