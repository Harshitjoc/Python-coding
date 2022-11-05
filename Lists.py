#hacker rank python question

if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        lst = input()
        lst = lst.split(" ")
        if lst[0]=="insert":
            arr.insert(int(lst[1]),int(lst[2]))
        elif lst[0]=="remove":
            arr.remove(int(lst[1]))
        elif lst[0]=="append":
            arr.append(int(lst[1]))
        elif lst[0]=="sort":
            arr.sort()
        elif lst[0]=="pop":
            arr.pop()
        elif lst[0]=="reverse":
            arr.reverse()
        elif lst[0]=="print":
            print(arr)  
