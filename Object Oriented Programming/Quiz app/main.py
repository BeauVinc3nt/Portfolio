from data import question_data  # importing stored data from external folder in project
from question_model import Question  # external imports
from quiz_brain import QuizBrain

# Creating a "question bank" filled with the questions and answers (initially empty to append as quiz progresses)
question_bank = []      

 # running for loop to generate word bank
for question in question_data: 
    question_text = question["text"]    # Specifying contents via keywords.
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer) # Creates a question by passing parameters into 'Question' object.
    question_bank.append(new_question)  # Adding new question structure (Q + A) for each piece of data and adding it to
                                        # the question bank list.

quiz = QuizBrain(question_bank)   # Creating quiz object.

# Game running while condition -> carry out function until while loop broken -> execute remaining code outside of while.
while quiz.still_has_questions():
    quiz.next_question()    # while condition is True, run next_question function.

# OUT OF WHILE LOOP (ONCE QUESTIONS ARE FINISHED, DISPLAY COMPLETION MESSAGE.)
print("You have completed the quiz!\n")
print(f"Your final score was {quiz.score} / {quiz.question_number}")
