
def get_student_info():
    name = input("what is your name? ").strip().title()
    sex = input("what is your sex?(m/f) ").upper()
    score = int(input("What did you score?: "))
    student = {'name': name, 'sex': sex, 'score': score}
    return student

def calc_avg(scores):
    return sum(scores)/len(scores)

def passed_students(database):
    students = {student['name']: student['score'] for student in database if student['score'] > 50}
    return students

def assign_grade(score):
    if score < 40:
        return 'F'
    elif (score >= 40) and (score < 50):
        return 'D'
    elif (score >= 50) and (score < 60):
        return 'C'
    elif (score >= 60) and (score < 70):
        return 'B'
    else:
        return 'A'

db = []
if __name__ == "__main__":
    # question 1
    for _ in range(3):
        student = get_student_info()
        db.append(student)
    print(db)

    # questions 2a
    scores = [student['score'] for student in db]
    print(calc_avg(scores))

    # question 2b
    for student in db:
        student['grade'] = assign_grade(student['score'])
    print(db)
