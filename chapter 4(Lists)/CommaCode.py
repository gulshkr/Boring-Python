# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.

# Solution:
def func(val):
    if len(val) == 0:
        return ''
    elif len(val) == 1:
        return val[0]
    else:
        return ', '.join(val[:-1]) + ', and ' + val[-1]

spam = ['apple','bananas','tofu','cats']
result = func(spam)
print(result) 