test_cases = int(input())

all_the_tests = {}
students_average = {}
average = 0
student_name = ""
for i in range(test_cases):
    student_scores = input().split()
    student_name = student_scores[0]

    i = 1
    scores = 0
    while i < len(student_scores):
        test_score = student_scores[i].split(":")
        test = test_score[0]
        score = float(test_score[1])

        scores += score

        if test not in all_the_tests:
            all_the_tests[test] = list()
        all_the_tests[test].append(score)
        i += 1


    students_average.update({student_name : (scores/(len(student_scores)-1))})

directory_items = students_average.items()

for x in sorted(directory_items):
    print(x[0],x[1])

for x in sorted(all_the_tests.items()):
    print(x[0], sum(x[1])/len(x[1]))






