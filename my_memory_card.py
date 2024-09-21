from PyQt5.Qtcore import Qt
from PyQt5.QtWidgets import Application, QWidget, QPushButton, QHBoxlayout, QVboxlayout, QLabel
QMessageBox, QRadioButton

app = QApplication({})
main_win = QWidget()
main_win.setWindowTitle('Memory card')
question = QLabel('Which nationality does not exist?')
RadioGroupBox = QGroupBox("Answer options")
rbtn_answer1 = QRadioButton('Enets')
rbtn_answer2 = QRadioButton('Chulyms')
rbtn_answer3 = QRadioButton('Smurfs')
rbtn_answer4 = QRadioButton('Aleuts')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addwidget(rbtn_answer1)
layout_ans2.addwidget(rbtn_answer2)
layout_ans3.addwidget(rbtn_answer3)
layout_ans3.addwidget(rbtn_answer4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

main_win.setLayout(layout_ans1)
main_woin.show()

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
answers = [rbtn_answer1, rbtn_answer2, rbtn_answer3, rbtn_answer4]
def ask(qst, right_answer, wrong1, wrong2, wrong3):
    from random import shuffle
    shuffle(answers)
    question.setText(qst)
    answers[0] = right_answer
    answer[1] = wrong1
    answer[2] = wrong2
    answer[3] = wrong3
    