from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_text():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()

def next_question():
    window.total += 1
    print('Статистика \n - Всего вопросов:', window, '\n - Правильных ответов:', window.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)


def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()



def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong_1)
    answer[2].setText(q.wrong_2)
    answer[3].setText(q.wrong_3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно')
        window.score += 1
        print('Статистика \n - Всего вопросов:', window.total, '\n - Правильных ответов:', window.score)
        print('Рейтинг:', (window.score // window.total)*100, '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неа')
            print('Рейтинг:', (window.score // window.total)*100, '%')


def show_correct(res):
    lb_Result.setText(res)
    show_result()



question_list = []
question_list.append(Question('Государственный язык Бразилии?', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
question_list.append(Question('Какого  цвета нету на флаге России?!!??? Аа???!!!', 'Зеленый', 'Белый', 'Красный', 'Синий'))
question_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))

app = QApplication([])
 
 
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(800, 600)
 
 

btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Какой национальности не существует?')
 
 
RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

AnsGroupBox = QGroupBox('Результаты теста:')
lb_Result = QLabel('Правильно/Не правильно')
lb_Correct = QLabel('Ответ')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignLeft | Qt.AlignTop
) 
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=2) 
AnsGroupBox.setLayout(layout_res)
 
RadioGroupBox.setLayout(layout_ans1)
 
 
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout() 
 
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)
 
 

layout_card = QVBoxLayout()
 
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) 
 

window.setLayout(layout_card)
window.cur_question = -1
btn_OK.clicked.connect(click_OK)

window.score = 0
window.total = 0

next_question()
window.show()
app.exec()
