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
        self.info_label = QLabel("")
        layout.addWidget(self.info_label)
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.ws = None
        self.connect_ws()

    def connect_ws(self):
        def run():
            try:
                self.ws = websocket.WebSocket()
                self.ws.connect(SERVER_URL)
                self.ws_connected = True
            except Exception as e:
                self.ws_connected = False
        threading.Thread(target=run, daemon=True).start()

    def send_request(self):
        if self.ws and self.ws_connected:
            try:
                self.ws.send("도움 요청")
                self.info_label.setText("요청이 전송되었습니다.")
            except Exception as e:
                self.info_label.setText("연결 오류")
        else:
            self.info_label.setText("서버 연결 중...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentApp()
    window.show()
    sys.exit(app.exec_())
