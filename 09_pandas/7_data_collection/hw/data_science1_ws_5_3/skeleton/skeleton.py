import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib3

# SSL 경고 비활성화
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 1. 웹페이지 가져오기
url = "https://news.seoul.go.kr/traffic/archives/1551"
response = requests.get(url, verify=False)  # get 메소드 사용 및 SSL 인증서 검증 비활성화
print("문제 1. 웹페이지 가져오기")
print("답: 상태 코드:", response.status_code)  # status_code 속성을 사용하여 상태 코드를 출력합니다.

# 2. 모든 테이블 찾기
soup = BeautifulSoup(response.text, 'html.parser')  # HTML 파서를 지정합니다.
tables = soup.select('table')  # 모든 <table> 태그를 찾습니다.
print("\n문제 2. 모든 테이블 찾기")
print(f"답: 찾은 테이블 수: {len(tables)}")  # tables의 길이를 출력합니다.

# 3. 각 테이블 처리
subway_data = {}
for i, table in enumerate(tables):
    title = table.find_previous('h5')  # 테이블 앞의 <h5> 태그를 찾습니다.
    table_name = title.text.strip() if title else f"Table {i + 1}"  # 테이블 이름을 설정합니다.

    data = [[td.text.strip() for td in tr.find_all(['th', 'td'])] for tr in table.find_all('tr')]  # 테이블의 모든 셀 내용을 추출합니다.
    max_cols = max(len(row) for row in data)  # 가장 긴 행의 길이를 찾습니다.
    data = [row + [''] * (max_cols - len(row)) for row in data]  # 모든 행의 길이를 동일하게 맞춥니다.

    df = pd.DataFrame(data[1:], columns=data[0])  # DataFrame을 생성합니다.
    subway_data[table_name] = df

print("\n문제 3. 테이블 데이터 추출 및 DataFrame 생성")
print(f"답: 처리된 테이블 수: {len(subway_data)}")  # 처리된 테이블의 수를 출력합니다.

# 4. 결과 출력
print("\n문제 4. 각 테이블의 요약 정보 출력")
for name, df in subway_data.items():  # 각 테이블에 대해 반복합니다.
    print(f"\n테이블 이름: {name}")
    print("답: 처음 5개 행")
    print(df.head())  # 각 DataFrame의 처음 5개 행을 출력합니다.
    print("\n" + "=" * 50)

# 5. 첫 번째 테이블에서 노선별 정보 추출
print("\n문제 5. 첫 번째 테이블에서 노선별 정보 추출")
if subway_data:
    first_table_name = list(subway_data.keys())[0]  # 첫 번째 테이블의 이름을 가져옵니다.
    operation_data = subway_data[first_table_name]  # 첫 번째 테이블의 데이터를 가져옵니다.


    print("답: 노선별 정보")
    for _, row in operation_data.iterrows():  # 각 행에 대해 반복합니다.
        if row.iloc[0] and row.iloc[0] != '구 분':  # 첫 번째 열이 비어있지 않고 '구 분'이 아닌 경우
            print(f"\n{row.iloc[0]}:")  # 노선 이름을 출력합니다.
            for col, val in row.items():  # 각 열에 대해 반복합니다.
                if col != row.iloc[0] and val:  # 첫 번째 열이 아니고 값이 있는 경우
                    print(f"  {col}: {val}")  # 열 이름과 값을 출력합니다.
