from PyQt5.QtWidgets import *
def menuWind():
    window = QDialog()
    questLbl = QLabel("Питання")
    questEdit = QLineEdit()

    rightAnswerLbl = QLabel("Правильна відповідь")
    questEdit2 = QLineEdit()

    nAnswerLbl = QLabel("Неправильна відповідь")
    questEdit3 = QLineEdit()


    n2AnswerLbl = QLabel("Неправильна відповідь")
    questEdit4 = QLineEdit()


    n3AnswerLbl = QLabel("Неправильна відповідь")
    questEdit5 = QLineEdit()
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
    def addFuns():
        base.qeust.append (
            {
                "питання": questEdit.text(),
                "Правильна відповідь": "",
                "не правильна1 ": "",
                "не правильна2 ": "",
                "не правильна3 ": ""
            }
        )
    mainLine.addWidget(addBtn)
    addBtn.clicked.connect(addFuns)

    window.setLayout(mainLine)
    window.show()
    window.exec()