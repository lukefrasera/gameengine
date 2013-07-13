import sys, os
import PyQt5.QtWidgets as qt
from mainWindow import *

def main():	
	app = qt.QApplication(sys.argv)
	w = mainWindow()
	w.show()

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()