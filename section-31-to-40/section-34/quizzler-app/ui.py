from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Georgia"
class QuizGUI:
    def __init__(self, quiz_brain : QuizBrain):
        self.window = Tk()      
        self.quiz_brain = quiz_brain
        self.score = 0
        self.flip_timer = 0
        self.setup_gui()
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def setup_gui(self):
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)

        self.score_label = Label(self.window, text=f"Score: {self.score}", bg=THEME_COLOR, fg="white", font=(FONT, 14))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_label = self.canvas.create_text(150, 125, width=280, text="Question Content", font=(FONT, 16, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

    def get_next_question(self):
        if self.quiz_brain.still_has_questions(): 
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_label, text=q_text)
        else:
            self.canvas.itemconfig(self.question_label, text="You've completed the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.score_label.config(text=f"Final Score: {self.score}/{len(self.quiz_brain.question_list)}")
        self.canvas.config(bg="white")

    def check_answer_true(self):
        is_correct = self.quiz_brain.check_answer("True")
        self.give_feedback(is_correct)
    def check_answer_false(self):
        is_correct = self.quiz_brain.check_answer("False")
        self.give_feedback(is_correct)
    
    def give_feedback(self, is_correct):
        if self.flip_timer:
            self.window.after_cancel(self.flip_timer)
            
        if is_correct :
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.flip_timer = self.window.after(5000, self.get_next_question)
