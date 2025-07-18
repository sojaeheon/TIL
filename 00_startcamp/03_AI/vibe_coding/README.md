# 학생-강사 실시간 알림 시스템 프로젝트

## 프로젝트 개요
학생들이 수업 중 모르는 것이 있을 때, 자신의 컴퓨터에서 아이콘을 클릭하면 강사 컴퓨터에 실시간으로 알림이 표시되는 시스템입니다. 이 시스템은 네트워크를 통해 학생과 강사 간의 실시간 소통을 지원합니다.

---

## 개발 워크플로우
1. **요구사항 분석 및 기획**
    - 학생: 질문/도움 요청 시 아이콘 클릭
    - 강사: 실시간으로 학생 요청 확인 및 응답
2. **기술 스택 선정**
    - 백엔드: Python (FastAPI 또는 Flask)
    - 프론트엔드: Electron.js (데스크탑 앱), 또는 PyQt
    - 실시간 통신: WebSocket
    - 배포: 실행파일(.exe) 생성 (PyInstaller 또는 Electron-builder)
3. **파일구조 설계**
4. **프로토타입 개발**
5. **기능 구현 및 테스트**
6. **실행파일 빌드 및 배포**

---

## 주요 기능
- 학생용 클라이언트: 아이콘 클릭 시 서버로 요청 전송
- 강사용 클라이언트: 실시간 알림 수신 및 시각적 표시
- 서버: 학생 요청 관리 및 강사에게 전달

---

## 기술 스택
- **Python 3.10+**
- **FastAPI**: REST API 및 WebSocket 서버
- **Electron.js** 또는 **PyQt**: 데스크탑 클라이언트
- **WebSocket**: 실시간 통신
- **PyInstaller/Electron-builder**: 실행파일(.exe) 빌드

---

## 파일구조 예시
```
vibe_coding/
├── README.md
├── server/
│   ├── main.py           # FastAPI 서버 및 WebSocket 핸들러
│   ├── requirements.txt  # 서버 의존성
├── client_student/
│   ├── main.py           # 학생용 클라이언트 (PyQt/Electron)
│   ├── icon.png          # 학생 아이콘
│   ├── requirements.txt  # 클라이언트 의존성
├── client_teacher/
│   ├── main.py           # 강사용 클라이언트 (PyQt/Electron)
│   ├── icon.png          # 강사 아이콘
│   ├── requirements.txt  # 클라이언트 의존성
└── build/
    └── ...               # 빌드된 실행파일(.exe)
```

---

## 개발 및 배포 과정
1. **서버 개발**: FastAPI 기반 WebSocket 서버 구현
2. **클라이언트 개발**: 학생/강사용 데스크탑 앱 개발 (PyQt/Electron)
3. **실행파일 빌드**: PyInstaller/Electron-builder로 .exe 생성
4. **테스트 및 배포**: 실제 환경에서 테스트 후 배포

---

## 향후 확장
- 학생별 요청 내역 관리
- 강사-학생 간 채팅 기능
- 모바일 앱 지원

---

## 참고
- 모든 소스코드는 Windows 환경 기준으로 작성
- 네트워크 환경(같은 Wi-Fi 등) 필요
- 실행파일(.exe)로 배포하여 설치 없이 바로 사용 가능

---

10년차 개발자의 경험을 바탕으로, 확장성과 유지보수성을 고려한 구조와 기술을 선정하였습니다. 추가 요구사항이나 세부 기능 요청 시 언제든 말씀해 주세요.
