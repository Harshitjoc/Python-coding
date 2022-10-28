#hacker rank python question

def swap_case(s):
    case = ''
    for i in s:
        if i.isupper():
            case += i.lower()
        elif i.islower():
            case += i.upper()
        else:
            case += i
    return case
