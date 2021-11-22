import random
questions = {}
score = 0
 
for i in range(10):
    value1= random.randint(0,99)
    value2= random.randint(0,99)
    operator_value = '+'
    question = str(value1)+''+ str('+')+''+ str(value2)
    answer = eval(question)
    question+=':  '

    questions.update({question:str(answer)})

for q in questions.keys():
    user_answer = input(q)
    if questions.get(q) == str(user_answer):
        score += 1
        print("You are Correct!!")
    else:
        print("You are Incorrect :(")
print(f"Your score is {str(score)} out of 10.")