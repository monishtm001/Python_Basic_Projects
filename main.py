from data import question_data
from question_model import Question

questions_bank=[]
for ques in question_data:
    Question_text=ques["text"]
    Question_answer=ques["answer"]
    newquestions=Question(Question_text,Question_answer)
    questions_bank.append(newquestions)
print(questions_bank)
