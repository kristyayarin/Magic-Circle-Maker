"""
import sys
sys.path.append("$NETHOME/maya/Qt_Dev")

import magic_circle_ui
reload(magic_circle_ui)

mayaWin = magic_circle_ui.getMayaMainWindow()
dialog = magic_circle_ui.McDialog(mayaWin) 
"""
# Aternatively, run this script directly from Cutter.
'''
isMaya = False
try:
	from PyQt4.QtCore import *
	from PyQt4.QtGui import *
	from PyQt4 import uic
except ImportError:
'''
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtUiTools import *
isMaya = True
import maya.OpenMayaUI as omui
import shiboken2
		
import sys
import os
import math
from connection_utils import *
import magic_circle_v02 as mc
reload (mc)

#________________________________________________________
# getMayaMainWindow
#________________________________________________________

def getMayaMainWindow():
	winPtr = omui.MQtUtil.mainWindow() #Returns Maya's main window.
	return shiboken2.wrapInstance(long(winPtr), QWidget) 
	#shiboken.wrapInstance(address, type)
	#Creates a Python wrapper for a C++ object instantiated at a given memory address 
	#- the returned object type will be the same given by the user.

#________________________________________________________
#                     Widget Names
#________________________________________________________
#                iconLabel
#     max_rad_dSBox    	max_rad_hSlider
#     min_rad_dSBox	    min_rad_hSlider
#     thick_dSbox       thick_hSlider
#     circle_checkBox
#
#     h_max_dSBox       h_max_hSlider
#     h_os_dSBox        h_os_hSlider
#     r_max_dSBox       r_max_hSlider
#     r_os_dSBox        r_os_hSlider
#
#                     pushButton
#________________________________________________________

class McDialog(QDialog):
	def __init__(self, parent=None):
		super(McDialog, self).__init__(parent)
		self.pathToIcon = os.path.join(os.path.dirname(__file__), 'icons', 'magic_circle_icon.jpg') #<<< Create Icon
		pathToUi = os.path.join(os.path.dirname(__file__), 'ui', 'magic_circle.ui')
		'''
		if isMaya == False:
			self.ui = uic.loadUi(pathToUi,self)
			self.setWindowFlags(Qt.WindowStaysOnTopHint)
		else:
		'''
		loader = QUiLoader()
		self.ui = loader.load(pathToUi, self)
		self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
		self.makeConnections()
		self.ui.show()
	#________________________________________________
	def makeConnections(self):
		
		#------------------------------------------------
		
		pixmap = QPixmap(self.pathToIcon)
		pixmap_resized = pixmap.scaled(400, 225)
		self.ui.iconLabel.setPixmap (pixmap_resized)
		self.ui.iconLabel.setMask (pixmap_resized.mask())
		
		#------------------------------------------------
		
		self.maxRad = FloatSlider(self.ui.max_rad_dSBox, self.ui.max_rad_hSlider, 2) 
		self.minRad = FloatSlider(self.ui.min_rad_dSBox, self.ui.min_rad_hSlider, 2) 
		self.thick = FloatSlider(self.ui.thick_dSbox, self.ui.thick_hSlider, 2) 
		self.hMax = FloatSlider(self.ui.h_max_dSBox, self.ui.h_max_hSlider, 2) 
		self.hOffset = FloatSlider(self.ui.h_os_dSBox, self.ui.h_os_hSlider, 2) 
		self.rMax = FloatSlider(self.ui.r_max_dSBox, self.ui.r_max_hSlider, 2) 
		self.rOffset = FloatSlider(self.ui.r_os_dSBox, self.ui.r_os_hSlider, 2) 
		self.ui.pushButton.clicked.connect(self.doitAction)
	#________________________________________________
	def doitAction(self):
	
		if self.ui.circle_checkBox.isChecked() == True :
			self.circleState = True
		else:
			self.circleState = False

		mc.magic_circle(self.maxRad.getValue(), self.minRad.getValue(), 
						self.thick.getValue(), self.hMax.getValue(),
						self.hOffset.getValue(), self.rMax.getValue(),
						self.rOffset.getValue(), self.circleState )
#========================================================		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	dialog = MatrixDialog()
	dialog.show()
	sys.exit(app.exec_())
