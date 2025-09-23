import requests
from bs4 import BeautifulSoup
import urllib3

# SSL 경고 비활성화
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 1. 웹페이지 가져오기
url = "https://topis.seoul.go.kr/map/openBusMap.do"
response = requests.get(url, verify=False)  # get 메소드 사용 및 SSL 인증서 검증 비활성화
print("문제 1. 웹페이지 가져오기")
print("답: 상태 코드:", response.status_code)  # status_code 속성을 사용하여 상태 코드를 출력합니다.
print("설명: 상태 코드 200은 웹페이지가 성공적으로 로드되었음을 의미합니다.")

# 2. <table> 태그 개수 세기
soup = BeautifulSoup(response.text, 'html.parser')  # HTML 파서를 지정합니다.
tables = soup.select('table')  # 모든 <table> 태그를 찾습니다.
print("\n문제 2. <table> 태그 개수 세기")
print("답: 테이블 개수:", len(tables))  # tables의 길이를 출력합니다.
print("설명: find_all() 메소드를 사용하여 모든 <table> 태그를 찾고, 그 개수를 계산했습니다.")


# 3. 첫 번째 <table>의 각 행 출력
print("\n문제 3. 첫 번째 <table>의 각 행 출력")
if tables:
    first_table = tables[1]  # 첫 번째 테이블을 선택합니다.
    rows = first_table.find_all('tr')  # 모든 <tr> 태그를 찾습니다
    print("답: 첫 번째 테이블의 행:")
    for row in rows:
        print("  -", row.text.strip())  # 각 행의 텍스트를 공백을 제거하여 출력합니다.
    print("설명: 첫 번째 <table>에서 모든 <tr> 태그를 찾고, 각 행의 텍스트를 공백을 제거하여 출력했습니다.")
else:
    print("답: 테이블이 존재하지 않습니다.")
    print("설명: 테이블을 찾지 못했기 때문에 출력할 행이 없습니다.")

# 4. 모든 <td> 태그 내용 추출
td_contents = [td.text.strip() for td in first_table.find_all('td') if td.text.strip()]  # 모든 <td> 태그의 내용을 추출하고 공백을 제거합니다.
print("\n문제 4. 모든 <td> 태그 내용 추출")
print("답: <td> 태그 내용:")
for content in td_contents:
    print("  -", content)
print("설명: <table> 내의 모든 <td> 태그에서 내용을 추출하고 공백을 제거했습니다.")

# 5. 데이터 정제 및 구분
print("\n문제 5. 데이터 정제 및 구분")
print(td_contents)
if td_contents:
    general_road = td_contents[1:5]  # 일반도로 기준 (마지막 '-' 포함)
    city_highway = td_contents[6:]  # 도시고속 기준 (5번 인덱스의 "도시고속" 제외)

    road_types = ["일반도로", "도시고속"]
    speed_meanings = ["원활", "서행", "정체", "정보없음"]
    print(general_road)
    print(city_highway)
    print("답: 정제된 데이터:")
    for i, road_type in enumerate([general_road, city_highway]):  # general_road와 city_highway를 순회합니다.
        print(f"{road_types[i]} 기준:")
        for j, speed in enumerate(road_type):
            if j < len(speed_meanings):  # speed_meanings의 길이를 확인합니다.
                print(f"  - {speed_meanings[j]}: {speed}")  # speed_meanings[j]와 speed를 출력합니다.
            else:
                print(f"  - 추가 정보: {speed}")

    print("설명: 추출된 데이터를 일반도로와 도시고속 기준으로 구분하고, 각 속도 범위의 의미를 추가하여 출력했습니다.")
else:
    print("답: 추출된 데이터가 없습니다.")
    print("설명: <td> 태그에서 추출된 데이터가 없어 정제할 내용이 없습니다.")
