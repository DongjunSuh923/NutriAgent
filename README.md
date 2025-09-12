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


### 3. 데이터베이스

- PostgreSQL with Docker

#### 1. 컨테이너 실행

컨테이너 시작
 docker start nutri-postgres

+ 상태 확인
 docker ps

#### 2. 데이터 적재
- venv 활성화 후
 python import_food_data.py
- data 폴더의 '20250408_음식DB.xlsx'에서 데이터 추출(약 29,000건)
- 가공 식품을 포함한 별도의 DB도 존재하므로 필요시 추가 가능


### 4. FastAPI

- 가상환경 활성화
 cd D:\Programming\Python\NutriAgent    # 필요시 개인 환경에 맞춰 경로 변경
 .\venv\Scripts\activate

 uvicorn app.main:app --reload

 - API 확인
  http://127.0.0.1:8000/search?query=검색어


### 5. React

 cd frontend
 (필요시 npm install)
 npm start

- 자동 실행
 http://localhost:3000