#hacker rank python question

if __name__ == '__main__':
    s = input()

    l = list(s)
    alnum = False
    al = False
    di = False
    lo = False
    up = False
    for i in l:
        if i.isalnum():
            alnum = True
        if i.isalpha():
            al = True
        if i.isalnum():
            alnum = True
        if i.isdigit():
            di = True
        if i.islower():
            lo = True
        if i.isupper():
            up = True
    print(alnum)
    print(al)
    print(di)
    print(lo)
    print(up)
