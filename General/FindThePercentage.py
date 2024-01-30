if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    sum=0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    for mark in marks:
        sum = sum+mark
    percentage = sum/3
    print(f'{percentage:.2f}')

