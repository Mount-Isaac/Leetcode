'''
Move the first letter of each word to the end of it, 
Then add "ay" to the end of the word. Leave punctuation marks untouched.
'''

def pig_it(text):
    '''    
    new_text = text.split(' ')

    for i in range(len(new_text)):
        if new_text[i].isalpha():
            element = new_text[i]
            element = element[1:] + f"{element[0]}ay"
            new_text[i] = element
    
    return ' '.join(new_text)

    The above runs with Tn O(n) and Space n of O(n) (it creates a new list out of the string)
    List comprehension builds a full memory using a Sn O(1) and Tn O(n)
    '''

    return ' '.join([f"{element[1:]}{element[0]}ay" if element.isalpha() else element for element in text.split(' ')])



print(pig_it('Pig latin is cool !'))
print(pig_it('hello!'))
print(pig_it('This is my string'))