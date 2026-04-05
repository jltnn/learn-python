if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    unique_scores = sorted(set(s[1] for s in students))
    if len(unique_scores) > 1:
        second_lowest_grade = unique_scores[1]
        results = [s[0] for s in students if s[1] == second_lowest_grade]
        results.sort()
        for name in results:
            print(name)
        
        
#Find the percentage practice:
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    target_query = student_marks[query_name]
    average = sum(target_query) / len(target_query)
    print(f"{average:.2f}")