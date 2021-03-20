# Quizzler
GUI Quiz app made using Python and Tkinter.

This program is an upgrade of a previous Quiz app I built. This time I added a User UI with the help of Tkinter
This UI can be found in the class QuizInterface inside the "ui.py" file.

To run this program simply run the "main.py" file. A window should appear with a large white square an the first question already
displayed inside it.

The questions displayed are all true or false type of questions. Therefore if the user thinks the answer is true, he can click on the green
check mark or if he thinks the answer is false, he can click on the red button with the X. The user's score is displayed at the top-right corner
of the window

If the answer selected by the user is correct (whether it was true or false), the canvas's color will change color from white to green. 
If the answer was incorrect, the canvas will turn red.

If the user had the right answer, his score on the top-right corner will increase by one, other wise it will remain the same.

The quiz ends when the user has been through all the questions of the quizz (10 questions as this is the amount specified in the parameters of our GET request).
