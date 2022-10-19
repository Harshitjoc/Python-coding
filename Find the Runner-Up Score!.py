#hacker rank python question

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
num = sorted(set(arr))
print(num[-2])
