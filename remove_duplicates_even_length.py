#!/usr/bin/python3

"""
Problem statement: Remove all the consecutive
duplicates when they occur in even number of
times

Few examples:
aebbcdeeezzzz :- aecdeee
aabcccddceeeff :- beee
"""


def remove_duplicates(text):
    text += '$' #End token
    temp_stack = []
    flag_count = 0
    for alpha in text:
        if not temp_stack:
            temp_stack.append(alpha)
        elif temp_stack[-1] == alpha:
            if flag_count:
                flag_count += 1
            else:
                flag_count = 2
            temp_stack.append(alpha)
        else:
            if flag_count and not flag_count % 2:
                lookup = temp_stack.pop()
                while temp_stack:
                    if temp_stack[-1] == lookup:
                        temp_stack.pop()
                    else:
                        break
                flag_count = 0
            else:
                flag_count = 0
            # Check if current alphabet has duplicates
            if temp_stack and temp_stack[-1] == alpha:
                flag_count += 2
            else:
                pass
            temp_stack.append(alpha)
    temp_stack.pop()
    return ''.join(temp_stack)


if __name__ == '__main__':
    inp = input("Enter a string: ")
    answer = remove_duplicates(inp)
    print(answer)