#!/usr/bin/python3

import re

"""
Problem statement: Encode a given string of expression
with the following rule:
1. + concatinate numbers. e.g. 1+2 gives 12
2. - concatinate and reverses. e.g. 1-2 gives 21
3. * concatinate and append a 0 at the end. e.g. 1*2 gives 120
4. / concatinate reverse and insert 0 between numbers  e.g. 1/2 gives 201

Few examples:
1*3-2/1 :- 102130
(2+3)*(4+5-4*6-0) :- 230460450
"""

def infix_to_postfix(exp):
    opstack = []
    out = []
    op_dict = {"+":1, "-":1, "*":2, "/":2}
    exp_list = re.findall(r"(\()|(\))|([\+\-\*\/])|(\d*)", exp)
    exp_list = [j for i in exp_list for j in i if j]
    for i in exp_list:
        if i.isdigit():
            out.append(i)
        else:
            if i in op_dict.keys():
                if opstack:
                    while opstack and op_dict.get(opstack[-1]) and op_dict[i] <= op_dict[opstack[-1]]:
                        if opstack:
                            out.append(opstack.pop())
                        else:
                            break
                    opstack.append(i)
                else:
                    opstack.append(i)
            elif i == '(':
                opstack.append(i)
            elif i == ')':
                while opstack[-1] != '(':
                    out.append(opstack.pop())
                opstack.pop()
    while opstack:
        out.append(opstack.pop())
    return out


def postfix_to_exp(p_exp):
    opstack = []
    op_list = ['+', '-', '*', '/']
    for i in p_exp:
        if i not in op_list:
            opstack.append(i)
        else:
            right = opstack.pop()
            left = opstack.pop()
            if i == '+':
                opstack.append(left + right)
            elif i == '-':
                opstack.append(right + left)
            elif i == '*':
                opstack.append(left + right + '0')
            elif i == '/':
                opstack.append(right + '0' + left)
    return opstack.pop()


if __name__ == "__main__":
    postfix = infix_to_postfix(str(input("Enter a expression: ")))
    exp = postfix_to_exp(postfix)
    print(exp)