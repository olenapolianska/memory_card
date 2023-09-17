import random
from PyQt5.QtWidgets import *
import memcard
import mem
import new
app = QApplication([])
app.setStyleSheet("""
        QWidget{
            background:#6CC7EE;
        }
        
        QPushButton
        {
            background-color: #78ff90;
            border-style:groove;
            font-family: cursive;
            min-width: 6em;
            padding: 6px;
            border-width:4px;
            border-color: #25BEFF;
            color:#074734
        }
        
    """)
window= QWidget()
mainLine = QVBoxLayout()
window.resize(500, 500)


menuBtn = QPushButton("Меню")
restBtn = QPushButton("Відпочити")
timeSpn = QSpinBox()
timeLbl = QLabel("хвилин")
pitanna = QLabel("Яблуко")
firstLine = QHBoxLayout()
firstLine.addWidget(menuBtn)
firstLine.addWidget(restBtn)
firstLine.addWidget(timeSpn)
firstLine.addWidget(timeLbl)
mainLine.addLayout(firstLine)
mainLine.addWidget(pitanna)


answersGroup = QGroupBox("Варіанти відповідей")
answer1 = QRadioButton("1")
answer2 = QRadioButton("2")
answer3 = QRadioButton("3")
answer4 = QRadioButton("4")
answers = [answer1,answer2,answer3,answer4]

answersLine = QVBoxLayout()
answersLine.addWidget(answer1)
answersLine.addWidget(answer2)
answersLine.addWidget(answer3)
answersLine.addWidget(answer4)
result = QLabel("Результат")
answersLine.addWidget(result)
result.hide()
answerBtn = QPushButton("Відповісти")
nextQBtn = QPushButton("Наступне питання")
editQBtn = QPushButton("Редагувати")
answersGroup.setLayout(answersLine)

mainLine.addWidget(answersGroup)
mainLine.addWidget(answerBtn)
mainLine.addWidget(nextQBtn)
mainLine.addWidget(editQBtn)
nextQBtn.hide()

def setQuest():
    random.shuffle(answers)
    pitanna.setText(memcard.quest[memcard.currentQuest]["питання"])
    answers[0].setText(memcard.quest[memcard.currentQuest]["Правильна відповідь"])
    answers[1].setText(memcard.quest[memcard.currentQuest]["не правильна1"])
    answers[2].setText(memcard.quest[memcard.currentQuest]["не правильна2"])
    answers[3].setText(memcard.quest[memcard.currentQuest]["не правильна3"])
setQuest()
def showResult():
    answers[0].hide()
    answers[1].hide()
    answers[2].hide()
    answers[3].hide()
    answerBtn.hide()
    result.show()
    nextQBtn.show()
    if answers [0].isChecked():
        result.setText("Правильно")
    else:
        result.setText("не правильно")

def nextFunc():
    random.shuffle(answers)
    answerBtn.show()
    answers[0].show()
    answers[1].show()
    answers[2].show()
    answers[3].show()
    result.hide()
    nextQBtn.hide()
    memcard.currentQuest += 1
    setQuest()

def editQuestFuns():
    window.hide()
    new.editWind()
    window.show()
    setQuest()
nextQBtn.clicked.connect(nextFunc)
answerBtn.clicked.connect(showResult)
menuBtn.clicked.connect(mem.menuWind)
editQBtn.clicked.connect(editQuestFuns)
window.setLayout(mainLine)
window.show()
app.exec()