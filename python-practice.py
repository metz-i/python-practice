def createStudent(name, scores=None):
    if scores is None:
        scores = []
        
    return {
        'name':name,
        'scores':scores
    }

amy = createStudent('amy')
dede = createStudent('dede')

def addScore(student, score):
    student['scores'].append(score)
    print(student['scores'])

addScore(amy, 90)
addScore(dede, 55)