def zero(f=None): return 0 if f else f(0)
def one(): pass #your code here
def two(): pass #your code here
def three(): pass #your code here
def four(): pass #your code here
def five(f=None): return f(5) if f else 5
def six(): pass #your code here
def seven(f=None): return f(7) if f else 7
def eight(): pass #your code here
def nine(): pass #your code here

def plus(): pass #your code here
def minus(): pass #your code here
def times(y): return lambda x : x * y
def divided_by(): pass #your code here


print(seven(times(five())))