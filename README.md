# 중고나라 자동 업로드

- 이 프로젝트는 중고나라에 게시글을 자동으로 업로드하는 프로그램입니다.
- 여러 상품의 리스팅 생성 및 게시 과정을 간소화합니다.

## 기술 스택 및 버전

- Python 3.8+
- Selenium 4.10.0
- pandas 1.5.3
- python-dotenv 1.0.0
- webdriver_manager 4.0.2

## 개발 환경

- macOS (M1 칩)

다른 운영 체제에서도 작동할 수 있지만, 일부 설정이나 코드 조정이 필요할 수 있습니다.

## 설정 방법

1. 이 저장소를 로컬 머신에 클론합니다.

2. 프로젝트 디렉토리로 이동합니다:
   ```
   cd joonggo_auto_upload
   ```

3. (선택사항) 가상 환경을 생성하고 활성화합니다:
   ```
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # 또는
   venv\Scripts\activate  # Windows
   ```

4. 필요한 의존성을 설치합니다:
   ```
   pip install -r requirements.txt
   ```

5. `.env.example` 파일의 이름을 `.env`로 변경하고 네이버 아이디와 비밀번호를 입력합니다:

   ```
   NAVER_ID=your_naver_id
   NAVER_PW=your_naver_password
   ```

   필요한 경우 Excel 파일 경로와 이미지 디렉토리도 수정할 수 있습니다:

   ```
   EXCEL_PATH=your_excel_file_path
   IMAGES_DIR=your_img_dir_name
   ```

6. 업로드하고자 하는 상품 정보를 Excel 파일에 정리합니다. `joongo_article_example.xlsx`를 템플릿으로 사용하세요.

7. 이미지 설정:
    - `images` 폴더 아래에 디렉토리 구조를 만듭니다.
    - 각 상품마다 별도의 하위 디렉토리를 만듭니다.
    - 하위 디렉토리 이름은 Excel 파일의 "디렉토리명" 열과 일치해야 합니다.

## 사용 방법

1. 메인 스크립트를 실행합니다:

   ```
   python main.py
   ```

2. 프로그램이 자동으로 다음 작업을 수행합니다:
    - 네이버 계정으로 로그인
    - 중고나라로 이동
    - Excel 파일의 각 상품에 대한 게시글 작성
    - 각 상품의 이미지 업로드
    - 게시글 제출

## 더 많은 중고나라 카테고리를 추가하려면

- 더 많은 중고나라 카테고리를 추가하려면 `mappings.py`의 `CATEGORIES` 딕셔너리를 수정하세요. 추가하려는 카테고리에 대한 올바른 `menuLink` 요소를 찾아야 합니다.

## 문제 해결

문제가 발생하면 `logs` 디렉토리의 로그 파일을 확인하여 자세한 정보를 얻을 수 있습니다.

## 면책 조항

이 도구는 개인 사용 목적으로만 제작되었습니다. 이 자동 게시 도구를 사용할 때는 중고나라의 서비스 약관을 준수해야 합니다.

## 기여

기여, 이슈 제기, 기능 요청은 언제나 환영합니다.

## 향후 계획

- 번개장터 등 다른 중고 플랫폼에 대한 지원이 향후 업데이트에 계획되어 있습니다.