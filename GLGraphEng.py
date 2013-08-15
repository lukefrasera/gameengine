from PyQt5.QtOpenGL import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QTimer

class view(QGLWidget):
	def __init__(self):
		super(view, self).__init__()
		self.time = QTime
		self.timer = QTimer

		self.setMouseTracking(True)
		self.setCursor(Qt.BlankCursor)
		self.setFocusPolicy(Qt.StrongFocus)

		self.timer.timeout.connect(self.tick)

	def initializeGL(self):pass
	def paintGL(self):pass
	def resizeGL(self):pass

	def mousePressEvent(self, e):pass
	def mouseMoveEvent(self, e):pass
	def mouseReleaseEvent(self, e):pass


	def keyPressEvent(self, e):
		if e.key() == Qt.Key_Escape:
			quit()

	def keyReleaseEvent(self, e):pass

	def tick(self):pass