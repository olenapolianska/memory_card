from PyQt5.QtWidgets import *
app = QApplication([])
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
answersLine = QVBoxLayout()
answersLine.addWidget(answer1)
answersLine.addWidget(answer2)
answersLine.addWidget(answer3)
answersLine.addWidget(answer4)


answersGroup.setLayout(answersLine)
mainLine.addWidget(answersGroup)
window.setLayout(mainLine)
window.show()
app.exec()