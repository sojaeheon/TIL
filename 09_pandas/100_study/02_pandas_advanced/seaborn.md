# 데이터 시각화 라이브러리 Seaborn
### 설치 방법
- pip install seaborn
- import seaborn as sns

## seaborn scatterplot 기본
- 기본적으로 x,y배열을 넣어주기만 하면 산점도를 그려준다

### Pandas 데이터프레임 지원
1. pandas 데이터 프레임 지원
- seaborn은 pandas 모듈의 데이터프레임 형식의 데이터를 시각화 해준다
- scatterplot의 data 인자에 `데이터프레임`을 넣고,
x와y인자에 데이터프레임이 갖고 있는 `컬럼`을 넣어주면 산점도를 쉽게 그릴 수 있다

2. 범주를 색상으로 표현(hue,hue_order)
- scatterplot의 hue인자를 설정하면 색상을 이용하여 범주를 표현할 수 있다.
- hue_oder에 범주값을 갖는 리스트를 넣어주면 해당 리스트 순서대로 색상과 범례를 표시해준다

3. 범주를 모양으로 구분(style,style_order)
- scatterplot의 style인자를 이용하면 범주를 모양으로 구분할 수 있다
- style_order는 hue_order와 동일한 방식으로 작동

4. 범주를 점 크기로 표현(size, size_order)
- scatterplot의 size인자를 이용하면 점(marker) 크기에 따라서 범주를 표현할 수 있다.
- size_order는 hue_order의 동작 방식과 같다.
