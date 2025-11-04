FROM python:3.10-slim                  # Python이 설치된 경량 베이스 이미지 사용
WORKDIR /workspace                     # 컨테이너 내부에서 작업할 디렉토리 지정
COPY requirements.txt .                # 로컬의 requirements.txt 파일을 컨테이너로 복사
RUN pip install --upgrade pip && \     # pip 업그레이드 및 패키지 설치
    pip install -r requirements.txt
COPY app.py .                          # 실행할 app.py 파일 복사
CMD ["python", "app.py"]               # 컨테이너 시작 시 실행할 명령 지정