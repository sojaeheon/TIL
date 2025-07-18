# 강사용 PyQt 클라이언트 뼈대
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import websocket
import threading

SERVER_URL = "ws://localhost:8000/ws"

class TeacherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("강사 클라이언트")
        self.label = QLabel("알림 없음")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.ws = None
        self.connect_ws()

    def connect_ws(self):
        def run():
            self.ws = websocket.WebSocket()
            self.ws.connect(SERVER_URL)
            while True:
                msg = self.ws.recv()
                self.label.setText(f"알림: {msg}")
        threading.Thread(target=run, daemon=True).start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TeacherApp()
    window.show()
    sys.exit(app.exec_())
