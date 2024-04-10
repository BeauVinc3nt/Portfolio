# Class for dealing with quiz ordering and points system.
class QuizBrain:       

    def __init__(self, q_list): # Constructor for class attributes (sets baseline attributes for objects.)
        self.question_number = 0    # Initial question number value (increments via for loop)
        self.question_list = q_list
        self.score = 0   # Setting initial score to 0. Increments with correct answers.

    def still_has_questions(self):
        return self.question_number < len(self.question_list)  # Checks that all questions have been asked.
        # Calculation determines whether 'still_has_questions' is true or False. (e.g. 5 < 12 --> True bool returned.)  

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1   # increments question number by 1 once function is ran.
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True or False):     ") # Creating question format.
        self.check_answer(user_answer, current_question.answer)

    # Answqer checking fucntion
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():   # Converting input and correct answer to lowercase for easy syntax.
            self.score += 1 # if correct answer, increment score by 1.
            print("\nCORRECT! You have earned a point.")
        else:
            print("\nINCORRECT! unfortunately that's incorrect.")   # If answer is wrong -> display message, no score increment.

        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score} / {self.question_number}\n\n") # print score out of total questions answered.