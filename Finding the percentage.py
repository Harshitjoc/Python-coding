#hacker rank python question

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    Total = 0
    count = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for key in student_marks.keys():
        if key == query_name:
            for value in student_marks[key]:
                Total += value
                count += 1
            average = Total/count
            print(f'{average:.2f}')
