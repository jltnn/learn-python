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
        
        
