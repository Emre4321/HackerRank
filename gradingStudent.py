def gradingStudents(grades):
    newscores = []
    for score in grades:
        dontround = False
        if score < 38:
            dontround = True
        elif str(score)[-1:] == "8" or str(score)[-1:] == "9" or str(score)[-1:] == "3" or str(score)[-1:] == "4" and dontround == False:
            score = round(score / 5) * 5
        newscores.append(score)
    return newscores

print(gradingStudents([4, 73, 67, 38, 33]))