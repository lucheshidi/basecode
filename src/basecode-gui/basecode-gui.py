from PyQt5.QtWidgets import *

# God! I have to use the slowly PyQt5 for gui version! F***!
def main():
    app = QApplication([])
    window = QMainWindow()   # Are you asking me why didn't I write the "parent" parameter? because I'm lazy :)
    window.show()
    window.setWindowTitle("basecode512 GUI")
    window.setBaseSize(512, 512)
    window.setMinimumSize(512, 512)
    window.centralWidget()
    return app.exec()

main()