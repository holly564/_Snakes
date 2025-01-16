import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QFrame, QLabel, QPushButton, \
    QLineEdit

# Create an instance of QApplication
app = QApplication(sys.argv)

# Create a QWidget instance (main window)
window = QWidget()
window.setWindowTitle('QFrame with Layout Managers Example')
window.setGeometry(100, 100, 400, 400)

# Create a QVBoxLayout instance for the main window
main_layout = QVBoxLayout()

# Create a QFrame with QVBoxLayout
vbox_frame = QFrame()
vbox_frame.setFrameShape(QFrame.Shape.Box)
vbox_frame.setFrameShadow(QFrame.Shadow.Plain)
vbox_layout = QVBoxLayout()
vbox_layout.addWidget(QLabel('Label in VBox'))
vbox_layout.addWidget(QPushButton('Button in VBox'))
vbox_frame.setLayout(vbox_layout)
main_layout.addWidget(QLabel('VBoxLayout'))
main_layout.addWidget(vbox_frame)

# Create a QFrame with QHBoxLayout
hbox_frame = QFrame()
hbox_frame.setFrameShape(QFrame.Shape.Box)
hbox_frame.setFrameShadow(QFrame.Shadow.Plain)
hbox_layout = QHBoxLayout()
hbox_layout.addWidget(QLabel('Label in HBox'))
hbox_layout.addWidget(QPushButton('Button in HBox'))
hbox_frame.setLayout(hbox_layout)
main_layout.addWidget(QLabel('HBoxLayout'))
main_layout.addWidget(hbox_frame)

# Create a QFrame with QGridLayout
grid_frame = QFrame()
grid_frame.setFrameShape(QFrame.Shape.Box)
grid_frame.setFrameShadow(QFrame.Shadow.Plain)
grid_layout = QGridLayout()
grid_layout.addWidget(QLabel('Label in Grid'), 0, 0)
grid_layout.addWidget(QPushButton('Button in Grid'), 0, 1)
grid_layout.addWidget(QLineEdit('Text in Grid'), 1, 0, 1, 2)
grid_frame.setLayout(grid_layout)
main_layout.addWidget(QLabel('GridLayout'))
main_layout.addWidget(grid_frame)

# Set the layout for the main window
window.setLayout(main_layout)

# Show the main window
window.show()

# Run the application's event loop
sys.exit(app.exec())