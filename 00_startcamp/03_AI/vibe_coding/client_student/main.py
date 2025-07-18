# 학생용 PyQt 클라이언트 뼈대
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import websocket
import threading

SERVER_URL = "ws://localhost:8000/ws"

class StudentApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("학생 클라이언트")
        self.button = QPushButton("도움 요청")
        self.button.clicked.connect(self.send_request)
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.ws = None
        self.connect_ws()

    def connect_ws(self):
        def run():
            self.ws = websocket.WebSocket()
            self.ws.connect(SERVER_URL)
        threading.Thread(target=run, daemon=True).start()

    def send_request(self):
        if self.ws:
            self.ws.send("도움 요청")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentApp()
    window.show()
    sys.exit(app.exec_())
