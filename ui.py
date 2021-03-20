from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # we must pass an object of type QuizBrain
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50, sticky="EW")
        self.question_text = self.canvas.create_text(150, 125, font="Arial 20 italic", text="Text",
                                                     fill=THEME_COLOR, width=280)
        true_image = PhotoImage(file="images/true.png")
        self.button_true = Button(image=true_image, highlightthickness=0, command=self.press_true)
        self.button_true.grid(column=0, row=2)
        false_image = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_image, highlightthickness=0, command=self.press_false)
        self.button_false.grid(column=1, row=2)
        self.score_label = Label(text="Score : 0 ", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.get_next_question()  # calls the function in order to avoid seeing placeholder

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")  # brings the canvas color to white again
        self.score_label.config(text=f"Score : {self.quiz.score}")  # updates the score

        if self.quiz.still_has_questions(): # checks if there are still questions left
            q_text = self.quiz.next_question()  # gets the next question
            self.canvas.itemconfig(self.question_text, text=q_text)  # displays the next question as text on canvas
        else:
            self.canvas.itemconfig(self.question_text, text="You've reach the end of the quiz ")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def press_true(self):
        is_right = self.quiz.check_answer("True")  # checks if the answer is true
        self.give_feedback(is_right)

    def press_false(self):
        is_right = self.quiz.check_answer("False")  # checks if the answer is false
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:  # if the correct answer was selected
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)



