from PyQt5 import uic, QtWidgets
from sys import path

def fucaoPrincipal():
    print('Apertou Botão!')

app = QtWidgets.QApplication([])
formulario = uic.loadUi('formulario.ui')
formulario.pushButton.clicked.connect(fucaoPrincipal)

formulario.show()
app.exec()