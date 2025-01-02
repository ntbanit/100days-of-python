from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

q_bank = []
for q in question_data:
    q_bank.append(Question(q["question"], q["correct_answer"]))

game = QuizBrain(q_bank)
while game.still_has_questions():
    right_answer = game.next_question()
game.end_game()