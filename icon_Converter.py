import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from PyQt5.QtCore import Qt
from PIL import Image

class ImageConverter(QWidget):
    def __init__(SELF):
        super().__init__()

        SELF.setWindowTitle('PNG To ICO Image Converter')
        SELF.setGeometry(800, 100, 400, 250)
        SELF.setStyleSheet("""
            background-color: #000000;  /* Black Background */
            color: #39FF14;  /* Neon Green Text */
            font-family: 'Courier New', Courier, monospace;  /* Retro Font */
        """)

        LAYOUT = QVBoxLayout()

        SELF.INFOLabel = QLabel('Select a PNG file to convert to ICO', SELF)
        SELF.INFOLabel.setAlignment(Qt.AlignCenter)
        SELF.INFOLabel.setStyleSheet("""
            font-size: 18px; 
            padding: 15px; 
            color:rgb(51, 250, 16);
        """)
        LAYOUT.addWidget(SELF.INFOLabel)

        SELF.SELECT_Button = QPushButton('Select PNG File', SELF)
        SELF.SELECT_Button.clicked.connect(SELF.select_png_file)
        SELF.SELECT_Button.setStyleSheet("""
            QPushButton {
                background-color: #39FF14;  /* Neon Green */
                color: black;
                padding: 12px;
                border-radius: 8px;
                font-size: 16px;
                border: 3px solid #39FF14;  /* Neon Green Border */
            }
            QPushButton:hover {
                background-color: #00FFFF;  /* Cyan Hover */
                border: 3px solid #00FFFF;  /* Cyan Border */
            }
        """)
        LAYOUT.addWidget(SELF.SELECT_Button)

        SELF.CONVERT_Button = QPushButton('Convert to ICO', SELF)
        SELF.CONVERT_Button.setEnabled(False)
        SELF.CONVERT_Button.clicked.connect(SELF.convert_to_ico)
        SELF.CONVERT_Button.setStyleSheet("""
            QPushButton {
                background-color: #FF073A;  /* Neon Red */
                color: black;
                padding: 12px;
                border-radius: 8px;
                font-size: 16px;
                border: 3px solid #FF073A;  /* Neon Red Border */
            }
            QPushButton:hover {
                background-color: #00FFFF;  /* Cyan Hover */
                border: 3px solid #00FFFF;  /* Cyan Border */
            }
        """)
        LAYOUT.addWidget(SELF.CONVERT_Button)

        SELF.setLayout(LAYOUT)

        # File paths
        SELF.png_file_path = None
        SELF.ico_file_path = None

    def select_png_file(SELF):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(SELF, "Select PNG File", "", "PNG Files (*.png);;All Files (*)", options=options)
        
        if file_path:
            SELF.png_file_path = file_path
            SELF.ico_file_path = file_path.rsplit('.', 1)[0] + '.ico'
            SELF.INFOLabel.setText(f'Selected: {file_path}\nReady to convert.')
            SELF.CONVERT_Button.setEnabled(True)

    def convert_to_ico(SELF):
        if SELF.png_file_path:
            try:
                with Image.open(SELF.png_file_path) as img:
                    img.save(SELF.ico_file_path, format='ICO')
                    SELF.INFOLabel.setText(f'Conversion successful!\nSaved as {SELF.ico_file_path}')
            except Exception as e:
                SELF.INFOLabel.setText(f'Error: {e}')
            SELF.CONVERT_Button.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    WIN = ImageConverter()
    WIN.show()
    sys.exit(app.exec_())
