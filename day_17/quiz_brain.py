class QueizBrain:
    def __init__(self,q_list):
        self.question_list = q_list
        self.question_no = 0
        self.score = 0    

    def still_has_question(self):
        return self.question_no < len(self.question_list)
        

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer =input(f"Q {self.question_no} : {current_question.text} True/False : ")
        self.check_answer(user_answer,current_question.answer)
    def check_answer(self,user_answer, answer):
        print(f"you type {user_answer}")
        if user_answer.lower() == answer.lower():
            print("you got it")
            self.score += 1
        else:
            print("wrong")
            print(f"answer was {answer}")
        print(f" your score is {self.score}/{self.question_no}")
