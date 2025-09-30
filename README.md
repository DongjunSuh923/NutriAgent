# NutriAgent

## 주의사항

- DB URL에 localhost 대신 127.0.0.1 사용 !! (Docker 환경 이슈로 URL이 localhost면 검색이 안될수도 있음)
- 서버 시작 순서
 1. Docker(Postgres)
 2. FastAPI
 3. React
    
- 의존성 설치시 반드시 (venv)가 표시되어 있는 CMD인지 확인할 것
- requirements.txt 참고, 간혹 일부 환경에서 인코딩 문제로 .xlsx 추출 스크립트가 작동을 안하는 경우가 있는 것으로 보임. 해결 방법 탐색 중..
- 만약 스크립트 실행이 안될 시 git lfs pull를 통해 업로드 되어있는 docker 컨테이너 복제본(nutri-postgres-backup.tar)을 로드해서 사용
```
docker load -i nutri-postgres-backup.tar
```

## 환경 세팅

### 1. 필수 설치

- [Python 3.13.x](https://www.python.org/downloads/)
- [Node.js & npm](https://nodejs.org/en/download)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/), 환경 차이 최소화를 위해 사용


### 2. 프로젝트 구조
```
NutriAgent/
├─ app/ # FastAPI
│ ├─ main.py
│ ├─ database.py
│ └─ models.py
├─ frontend/ # React
│ ├─ src/
│ │ └─ App.js
│ │ └─ App.css
│ │ └─ App.test.js
│ │ └─ index.css
│ │ └─ index.js
│ │ └─ logo.svg
│ │ └─ reportWebVitals.js
│ │ └─ setupTests.js
│ └─ package.json
├─ data/
│ └─ 20250408_음식DB.xlsx
│ └─ 20250327_가공식품DB_147999건.xlsx
│ └─ 국가표준식품성분표_250426공개.xlsx
├─ routers/
│ └─ foods.py
├─ import_food_data.py # .xlsx -> DB 적재 스크립트
├─ import_processed_food_data.py # .xlsx -> DB 적재 스크립트
├─ import_standard_food_data.py # .xlsx -> DB 적재 스크립트
├─ requirements.txt
└─ README.md
```

### 3. 데이터베이스

- PostgreSQL with Docker

#### 1. 컨테이너 실행

최초 1회
```
docker run --name nutri-postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=1234 -e POSTGRES_DB=nutri_db -p 5432:5432 -d postgres:15
```
이후 컨테이너 시작
```
docker start nutri-postgres
```

+ 상태 확인
```
docker ps
```

#### 2. 데이터 적재
- venv 활성화 후
```
python import_food_data.py
```
- data 폴더의 '20250408_음식DB.xlsx' 외 2개를 스크립트 'import_~_food_data.py' 3개를 각각 최초 1회 실행해 추출


### 4. FastAPI

- 가상환경 활성화
```
cd D:\Programming\Python\NutriAgent    # 필요시 개인 환경에 맞춰 경로 변경
.\venv\Scripts\activate
uvicorn app.main:app --reload
```

 - API 확인
  http://127.0.0.1:8000/search?query=검색어


### 5. React
```
cd frontend
(필요시 npm install)
npm start
```

- 자동 실행
 http://localhost:3000


### 6. 예시

#### Docker
<img width="1111" height="622" alt="image" src="https://github.com/user-attachments/assets/d04e884f-1879-4d63-85c9-44af24b136a4" />
<img width="1265" height="716" alt="image" src="https://github.com/user-attachments/assets/bb6a9ef4-7bda-4e88-82d3-666782aa6cc4" />

#### FastAPI (실행 및 http://127.0.0.1:8000/search?query=소고기 접속 결과)
<img width="1481" height="480" alt="image" src="https://github.com/user-attachments/assets/805daeec-dcc9-4d1b-82bc-ba5e5e54869e" />
<img width="1919" height="910" alt="image" src="https://github.com/user-attachments/assets/074a7f98-d054-4ebb-a429-0de0e5948bf6" />


#### React (실행 및 '소고기' 검색 결과)
<img width="1479" height="483" alt="image" src="https://github.com/user-attachments/assets/0de712bd-e73f-4048-9c87-27d91375d6cb" />
<img width="1919" height="912" alt="image" src="https://github.com/user-attachments/assets/08194b3f-83c2-4389-bf41-078e0de2ee16" />



