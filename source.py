import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QColor, QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


def resource_path(relative_path):
   try:
      base_path = sys._MEIPASS
   except Exception:
      base_path = os.path.abspath(".")

   return os.path.join(base_path, relative_path)

def window():
   app = QApplication(sys.argv)
   w = QWidget()

   #windowsize
   w.setFixedSize(600,250)

   #Background
   BG = QLabel(w)
   BG.setGeometry(0,0,600,250)
   BG.setPixmap(QPixmap(resource_path("bfur.png")).scaled(600,250))
   BGembed = QVBoxLayout()
   BGembed.addWidget(BG)
   w.setLayout(BGembed)

   #Title text
   b = QLabel(w)
   b.setText("Bhop Sensitivity Converter")
   fSize = QFont()
   fSize.setPointSize(18)
   b.setFont(fSize)
   b.move(20,20)
   b.adjustSize()

   #DPI INPUT
   dpi_input = QLineEdit(w)
   dpi_input.setFixedSize(80,30)
   dpi_font = QFont()
   dpi_font.setPointSize(10)
   dpi_input.setFont(dpi_font)
   dpi_input.move(270,120)
   dpi_input.setPlaceholderText("Current DPI")

   #DPI Desired
   dpiD = QLineEdit(w)
   dpiD.setFixedSize(80,30)
   dpiD_font = QFont()
   dpiD_font.setPointSize(10)
   dpiD.setFont(dpiD_font)
   dpiD.move(270,180)
   dpiD.setPlaceholderText("Desired DPI")

   #Current yaw
   yaw_current = QLineEdit(w)
   yaw_current.setFixedSize(90,30)
   yaw_current_f = QFont()
   yaw_current_f.setPointSize(10)
   yaw_current.setFont(yaw_current_f)
   yaw_current.setPlaceholderText("Current yaw")
   yaw_current.move(120,120)

   #Desired yaw
   yaw_d = QLineEdit(w)
   yaw_d.setFixedSize(90,30)
   yaw_d_f = QFont()
   yaw_d_f.setPointSize(10)
   yaw_d.setFont(yaw_d_f)
   yaw_d.move(120,180)
   yaw_d.setPlaceholderText("Desired yaw")

   #Current Sens
   sens = QLineEdit(w)
   sens.setFixedSize(90,30)
   sens_f = QFont()
   sens_f.setPointSize(10)
   sens.setFont(sens_f)
   sens.move(400,155)
   sens.setPlaceholderText("Current Sens")

   #Result text
   result = QLabel(w)
   result.setText("Converted sensitivity:")
   result_f = QFont("White")
   result_f.setPointSize(10)
   result.setFont(result_f)
   palette = result.palette()
   palette.setColor(QPalette.WindowText, QColor("white"))
   result.setPalette(palette)
   result.move(330,50)
   result.adjustSize()

   #Results box
   conv = QPushButton(w)
   conv.setText("Convert")
   conv.setFixedSize(60,35)
   conv.move(510,200)

   #credits
   credits = QLabel(w)
   credits.setText("made by messi lionel")
   credits_f = QFont()
   credits_f.setPointSize(10)
   credits.setFont(credits_f)

   credits_palette = credits.palette()
   credits_palette.setColor(QPalette.WindowText, QColor("white"))
   credits.setPalette(credits_palette)

   credits.move(15,220)
   credits.adjustSize()


   #Results Display
   result_display = QLineEdit(w)
   result_display.setText("")
   result_display_f = QFont()
   result_display_f.setPointSize(10)
   result_display.setFont(result_display_f)
   result_display.setPalette(palette)
   result_display.move(330,80)
   result_display.adjustSize()
   result_display.setReadOnly(True)

   def calculate():
      # Maths
      try:
         current_dpi = float(dpi_input.text())
         desired_dpi = float(dpiD.text())
         current_sens = float(sens.text())
         current_yaw = float(yaw_current.text())
         desired_yaw = float(yaw_d.text())

         new_sens = (current_dpi / desired_dpi) * (current_yaw / desired_yaw) * current_sens
         result_display.setText(f"{new_sens:.2f}")

      except ValueError:
         result_display.setText("Invalid Input")
         result_display.adjustSize()

   conv.clicked.connect(calculate)


   w.setWindowTitle("Bhop Sens Converter")
   w.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()


