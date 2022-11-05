#hacker rank python question

row , column = list(map(int,input().split()))
middle = row // 2
x = 1
for i in range(middle):
    print(('.|.' * x).center(column,'-'))
    x+=2
x-=2
print('WELCOME'.center(column,'-'))
for i in range(middle):
    print(('.|.' * x).center(column,'-'))
    x-=2
