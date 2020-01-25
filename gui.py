import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QMessageBox, QSpinBox
from app import main

class Window(QWidget):
  def __init__(self):
    # initialize
    QWidget.__init__(self)
    self.width = 300
    self.height = 500
    # select pdf
    self.selectPDFButton = QPushButton("Select PDF File", self)
    self.selectPDFButton.move(85, 40)
    self.selectPDFButton.clicked.connect(self.selectPDF)
    # spinner
    self.sp = QSpinBox()
    
  def selectPDF(self):
    fname = QFileDialog.getOpenFileName(self, 'Open file', '/home', '*.pdf')
    
    # check if user selected a file
    if fname[0]:
      # check if user selected a PDF
      if fname[0].split('.')[-1] == 'pdf':
        return main(fname[0])
      else:
        QMessageBox.critical(
          self,
          "Invalid file type",
          "Selected file can only be PDFs, if you want to suggest other extensions, please head over to https://github.com/FelixIsaac/audible-pdfs/pulls and suggests"
        )
        
if __name__ == "__main__":
  # Initialize
  app = QApplication(sys.argv)
  # GUI
  window = Window()
  window.setWindowTitle('Audible PDFs')
  window.setGeometry(500, 500, 250, 80)
  window.show()
  # Main loop
  sys.exit(app.exec_())