import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtGui, QtCore

widgets = {
    "logo": [],
    "button": [],
    "score": [],
    "question": [],
    "pergunta1": [],
    "pergunta2": [],
    "pergunta3": [],
    "pergunta4": [],

}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Quem quer ser programador?")
window.setFixedWidth(1000)
window.move(200, 0)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()

def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

def star_game():
    clear_widgets()
    frame2()

def show_frame1():
    clear_widgets()
    frame1()

def createButtons(pergunta, l_margin, r_margin):
        button = QPushButton('pergunta')
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setFixedWidth(485)
        button.setStyleSheet(
            "*{border: 4px solid '#BC006C';" +
            "margin-left: " + str(l_margin) + "px;" +
            "margin-right: " + str(r_margin) + "px;" +
            "color: white;" +
            "font-family: 'shanti';" +
            "border-radius: 25px;" +
            "padding: 15px 0;" +
            "margin-top: 20px}"+
            "*:hover{background: '#bc006C'}"
        )
        button.clicked.connect(show_frame1)
        return button


def frame1():
    #display Logo
    image = QPixmap("trivia\logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 200px; margin-bottom: 100px")
    widgets["logo"].append(logo)

    #bottum widget
    button = QPushButton("PLAY")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{border: 4px solid '#BC006C';" +
        "border-radius: 30px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 10px 0;" +
        "margin: 100px 300px;}" +
        "*:hover{background: '#BC006C';}"
    )
    button.clicked.connect(star_game)
    widgets["button"].append(button)


    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)

def frame2():
    score = QLabel("80")
    score.setAlignment(QtCore.Qt.AlignRight)
    score.setStyleSheet(
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 20px 15px;" +
        "margin: 50px 200px;" +
        "background: '#64A314';" +
        "border: 1px solid '#64A314';" +
        "border-radius: 40px;"
    )
    widgets["score"].append(score)

    question = QLabel("Coloque aqui o texto que vai aqui!")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 75px;"

    )
    widgets["question"].append(question)
    
    button1 = createButtons('pergunta1', 85, 5)
    button2 = createButtons('pergunta2', 5, 85)
    button3 = createButtons('pergunta3', 85, 5)
    button4 = createButtons('pergunta4', 5, 85)

    widgets["pergunta1"].append(button1)
    widgets["pergunta2"].append(button2)
    widgets["pergunta3"].append(button3)
    widgets["pergunta4"].append(button4)

    image = QPixmap("trivia\logo_bottom.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 50px; margin-bottom: 10px;")
    widgets["logo"].append(logo)

    grid.addWidget(widgets["score"][-1], 0, 1)
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["pergunta1"][-1], 2, 0)
    grid.addWidget(widgets["pergunta2"][-1], 2, 1)
    grid.addWidget(widgets["pergunta3"][-1], 3, 0)
    grid.addWidget(widgets["pergunta4"][-1], 3, 1)
    grid.addWidget(widgets["logo"][-1], 4, 0, 1 , 2)

frame1()
window.setLayout(grid)

window.show()
sys.exit(app.exec())