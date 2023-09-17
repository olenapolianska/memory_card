from PyQt5.QtWidgets import *

import memcard

def editWind():
    window = QDialog()
    questLbl = QLabel("Питання")
    questEdit = QLineEdit()
    questEdit.setText(memcard.quest[memcard.currentQuest]["питання"])

    rightAnswerLbl = QLabel("Правильна відповідь")
    questEdit2 = QLineEdit()
    questEdit2.setText(memcard.quest[memcard.currentQuest]["Правильна відповідь"])

    redBtn = QPushButton("Редагувати")

    nAnswerLbl = QLabel("Неправильна відповідь")
    questEdit3 = QLineEdit()
    questEdit3.setText(memcard.quest[memcard.currentQuest]["не правильна1"])

    n2AnswerLbl = QLabel("Неправильна відповідь")
    questEdit4 = QLineEdit()
    questEdit4.setText(memcard.quest[memcard.currentQuest]["не правильна2"])
    n3AnswerLbl = QLabel("Неправильна відповідь")
    questEdit5 = QLineEdit()
    questEdit5.setText(memcard.quest[memcard.currentQuest]["не правильна3"])
    addBtn = QPushButton("Меню")

    mainLine = QVBoxLayout()

    h1 = QHBoxLayout()
    h1.addWidget(questLbl)
    h1.addWidget(questEdit)
    mainLine.addLayout(h1)
    h2 = QHBoxLayout()
    h2.addWidget(rightAnswerLbl)
    h2.addWidget(questEdit2)
    mainLine.addLayout(h2)

    h3 = QHBoxLayout()
    h3.addWidget(nAnswerLbl)
    h3.addWidget(questEdit3)
    mainLine.addLayout(h3)

    h4 = QHBoxLayout()
    h4.addWidget(n2AnswerLbl)
    h4.addWidget(questEdit4)
    mainLine.addLayout(h4)

    h5 = QHBoxLayout()
    h5.addWidget(n3AnswerLbl)
    h5.addWidget(questEdit5)

    mainLine.addLayout(h5)

    mainLine.addWidget(redBtn)
    def addFuns():
        memcard.quest[memcard.currentQuest]={
            "питання": questEdit.text(),
            "Правильна відповідь": questEdit2.text(),
            "не правильна1": questEdit3.text(),
            "не правильна2": questEdit4.text(),
            "не правильна3": questEdit5.text()
        }
        window.close()

    redBtn.clicked.connect(addFuns)
    window.setLayout(mainLine)
    window.show()
    window.exec()