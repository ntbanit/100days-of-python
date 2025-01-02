class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        q = self.question_list[self.question_number]
        print(f"Question: {q.text}")
        choice = input("Choose true or false?: ").lower()
        if choice == q.answer.lower() :
            self.score += 1
        self.question_number += 1
        print(f"Correct answer: {q.answer}")
        print(f"Your score: {self.score}/{self.question_number}")
        return False

    def end_game(self):
        print("You've completed the quiz")
        print(f"Your final score was: {self.score}/{self.question_number}")