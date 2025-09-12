# NutriAgent

## 주의사항

- DB URL에 localhost 대신 127.0.0.1 사용 !! (Docker 환경 이슈로 URL이 localhost면 검색이 안되는 걸로 추정)
- 서버 시작 순서
 1. Docker(Postgres)
 2. FastAPI
 3. React


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
│ └─ models_orm.py
├─ frontend/ # React
│ ├─ src/
│ │ └─ App.js
│ └─ package.json
├─ data/
│ └─ 20250408_음식DB.xlsx # 국내 음식 DB, 가공 식품 데이터 미포함
├─ import_food_data.py # .xlsx -> DB 적재 스크립트
└─ README.md
```

### 3. 데이터베이스

- PostgreSQL with Docker

#### 1. 컨테이너 실행

컨테이너 시작
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
- data 폴더의 '20250408_음식DB.xlsx'에서 데이터 추출(약 29,000건)
- 가공 식품을 포함한 별도의 DB도 존재하므로 필요시 추가 가능


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
<img width="1919" height="991" alt="image" src="https://github.com/user-attachments/assets/f5570ddd-21ab-4e35-8a04-738b0aaa6de8" />

#### React (실행 및 '소고기' 검색 결과)
<img width="1479" height="483" alt="image" src="https://github.com/user-attachments/assets/0de712bd-e73f-4048-9c87-27d91375d6cb" />
<img width="1919" height="990" alt="image" src="https://github.com/user-attachments/assets/ec213fef-ca8c-46ae-baa0-979e88d7666b" />
<img width="1919" height="912" alt="image" src="https://github.com/user-attachments/assets/08194b3f-83c2-4389-bf41-078e0de2ee16" />



