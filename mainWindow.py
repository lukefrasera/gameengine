from PyQt5.QtWidgets import *
import GLGraphEng as GGE

class mainWindow(QMainWindow):
	def __init__(self):
		super(mainWindow, self).__init__()

		central = GGE.view()
		self.loadView(central)

	def loadView(self, widget):
		self.showFullScreen()
		self.setCentralWidget(widget)