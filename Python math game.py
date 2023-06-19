from random import randint


def calculateAnswer(ln,rn,operator):
    if ( operator == "+"):
        return ln + rn
    if ( operator == "-"):
        return ln - rn
    if ( operator == "*"):
        return ln * rn
    if ( operator == "/"):
        return ln / rn
    raise Exception("Operator Unknown")
    


def generateQuestion():
    ops = "/*-+"
    OpIndex = randint(0,len(ops)-1)
    ln = randint(0,10)
    rn = randint(0,10)
    operator = ops[OpIndex]
    while (rn == 0 and operator == "/"):
        rn = randint(0,10)
    return ln,rn,operator




question = generateQuestion()
correctAnswer = calculateAnswer(question[0],question[1],question[2])
playerAnswer =  input("{0}{1}{2}=?".format(question[0],question[2],question[1]))

if (str(correctAnswer) == playerAnswer):
    print("correct")
else:
    print("Wrong. Correct Answer is " + str(correctAnswer))
        


