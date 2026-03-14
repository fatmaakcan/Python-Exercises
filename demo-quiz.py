class Question:
    def __init__(self,text,choices,answer): 
        self.text=text
        self.choices=choices
        self.answer=answer

    def checkAnswer (self,answer):
        return str(self.answer)==str(answer)


class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestions(self):
        question=self.getQuestion()
        print(f'Question {self.questionIndex+1}/{len(self.questions)}: {question.text}')

        for q in question.choices:
            print(f'-  {q}')
        answer=input('Please enter the answer: ')
        self.guess(answer)
    
    def guess(self,answer):
        question=self.getQuestion()

        if question.checkAnswer(answer):
            self.score+=1
            print("Correct!")
        self.questionIndex+=1
        

        if self.questionIndex<len(self.questions):
            self.displayQuestions()
        else:
            print(f"Quiz finished! Your score: {self.score}/{len(self.questions)}")
      
        

q1=Question("How many countries are in the world?",[195,215,175,230],"195")
q2=Question("Which country is the smallest by area?",["Italy","Singapoure","Andorra","Vatican"],"Vatican")
q3=Question("When did The Beatles break up?",[1965,1970,1980,1990],"1970")
questionList=[q1,q2,q3]

quiz=Quiz(questionList)

quiz.displayQuestions()
