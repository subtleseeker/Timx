import sys, time, pygame
from PyQt4 import QtGui, QtCore, uic

SONG_END = pygame.USEREVENT + 1

class Window(QtGui.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		uic.loadUi('gui.ui',self)
		self.home()

	def home(self):
		# QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))

		# self.setCentralWidget(self.widget)
		# widget.resize()
		pygame.mixer.init()
		pygame.mixer.music.load("./assets/audio/tick.wav")

		self.setWindowIcon(QtGui.QIcon('./assets/icon/timx.png'))

		self.add15m.clicked.connect(lambda: self.addMin(15))
		self.add10m.clicked.connect(lambda: self.addMin(10))
		self.add5m.clicked.connect(lambda: self.addMin(5))

		self.addQButton.clicked.connect(self.onQPlus)
		self.resetButton.clicked.connect(self.onReset)
		self.startButton.clicked.connect(self.onStart)

		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.countDown)

		self.volumeButton.clicked.connect(self.onMute)

		self.show()

	def onMute(self):
		text = self.volumeButton.text()

		if(text == "Mute"):
			self.volumeButton.setText("Unmute")
			pygame.mixer.music.set_volume(0)
			# self.volumeButton.setIcon("")	
			
			# pygame.mixer.music.load("tick.wav")

		if(text == "Unmute"):
			self.volumeButton.setText("Mute")
			pygame.mixer.music.set_volume(1)
			

	def addMin(self, add_mins):
		global mins, secs, time
		time = self.lineEdit.text()
		mins = int((time.split(':'))[0])
		mins+=add_mins
		secs = int((time.split(':'))[1])
		time = str(mins).zfill(2) + ":" + str(secs).zfill(2)
		self.lineEdit.setText(time)


	def onReset(self):
		self.lineEdit.setText("15:00")
		self.startButton.setText("Start")
		self.onPause()
		self.elapsedTimeLabel.setText("00:00")

	def onStart(self):
		text = self.startButton.text()
		global mins, secs, time

		time = self.lineEdit.text()
		print(time)
		mins = int((time.split(':'))[0])
		secs = int((time.split(':'))[1])

		if(text == "Start"):
			self.startButton.setText("Pause")
			self.timer.start(1000)	
			
			pygame.mixer.music.load("./assets/audio/tick.wav")
			pygame.mixer.music.play(-1)

		if(text == "Pause"):
			self.startButton.setText("Start")
			pygame.mixer.music.stop()
			self.timer.stop()
			# self.startButton.clicked.connect(self.timer.stop())
			
		print(text)

	def onPause(self):
		self.timer.stop()
		pygame.mixer.music.stop()

	def countDown(self):
		global mins, secs, time
		if secs>0:
			secs-=1
			self.elapsedTime()
		elif mins>0:
				mins-=1
				secs=59
				self.elapsedTime()
		else:
			self.timer.stop()

			pygame.mixer.music.stop()
			pygame.mixer.music.load("./assets/audio/beep.wav")
			pygame.mixer.music.set_volume(1)
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				continue
			if self.volumeButton.text()=="Unmute":
				pygame.mixer.music.set_volume(0)

		
			self.startButton.setText("Start")
			stop = QtGui.QMessageBox.warning(self,"Time is up", "Boom")

		# time = str("{:2d}:{:2d}".format(mins, secs)) #Python3
		time = str(mins).zfill(2)+':'+str(secs).zfill(2)
		# print(time+"^^")
		self.lineEdit.setText(time)

	def onQPlus(self):
		num = int(self.labelQNum.text())
		self.labelQNum.setNum(num+1)
		self.onReset();
		print(num+1)

		self.textEdit.append("Q"+ self.labelQNum.text() +": "+ eTime)

	def elapsedTime(self):
		global eTime
		eTime = self.elapsedTimeLabel.text()
		eMins = int((eTime.split(':'))[0])
		eSecs = int((eTime.split(':'))[1])

		eSecs += 1
		if eSecs > 59:
			eSecs = 0
			eMins +=1

		eTime = str(eMins).zfill(2)+':'+str(eSecs).zfill(2)
		self.elapsedTimeLabel.setText(eTime)
		return eTime


	def close_application(self):
		quit = QtGui.QMessageBox.question(self, 'Quit', "Do you want to quit the application?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

		if quit == QtGui.QMessageBox.Yes:
			print("Quitting now")
			sys.exit()
		else:
			pass
	


def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	app.exec_()
	# app.deleteLater()
	sys.exit()


run()


