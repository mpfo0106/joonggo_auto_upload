import os
from dotenv import load_dotenv

# 프로젝트 루트 디렉토리 경로 설정
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# .env 파일 로드
load_dotenv(os.path.join(PROJECT_ROOT, ".env"))

# 상대 경로 설정
EXCEL_PATH = os.path.join(
    PROJECT_ROOT, os.getenv("EXCEL_PATH", "data/joonggo_article.xlsx")
)
IMAGES_DIR = os.path.join(PROJECT_ROOT, os.getenv("IMAGES_DIR", "images"))

# 아이디 설정
NAVER_ID = os.getenv("NAVER_ID")
NAVER_PW = os.getenv("NAVER_PW")
