def gradingStudents(grades):
    grades.pop(0)
    newscores = []
    for score in grades:
        if score % 5 > 2 and score > 37:
            score = round(score / 5) * 5
        newscores.append(score)
    return newscores


print(gradingStudents([4, 73, 67, 38, 33]))

