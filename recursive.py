def find_names_recursive(student_list, target_score):
    if not student_list:
        return[]
    first_student = student_list[0]
    rest_of_students = student_list[1:]
    if first_student[1] == target_score:
        return [first_student[0]] + find_names_recursive(rest_of_students, target_score)
    else:
        return find_names_recursive(rest_of_students, target_score)
    
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    unique_scores = sorted(set(s[1] for s in students))
    if len(unique_scores) > 1:
        second_highest_grade = unique_scores[-2]
        results = find_names_recursive(students, second_highest_grade)
        results.sort()
        for name in results:
            print(name)
