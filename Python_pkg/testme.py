# x = int(input('Enter First Value:'))
# y = int(input('Enter Second Value:'))
#
# def addition(x,y):
#     return x+y
#
# add = addition(x,y)
# print(add)

# ch = input('enter the char')
# print(ch[0])

import ast

def input_detect(s):
    return ast.literal_eval(input(s))

s = input('Enter the value')
result = input_detect(s)
print(dtype(result))
