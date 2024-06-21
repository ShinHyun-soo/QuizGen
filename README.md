| No | 항목 | 설명 | 기능 요구사항 |
|----|-----|------|-------------|
| 1  | 5지 선다형 | 객관식 답의 개수를 임의로 설정할 수 있는 기능 | 사용자가 최소 2개에서 최대 5개까지 답안 개수를 설정 |
| 2  | 다수 정답 UI 및 채점 기능 | 답의 개수가 2개 이상일 경우, 다수 정답을 선택할 수 있도록 UI 제공 및 채점 | 다수 정답을 선택할 수 있는 멀티 셀렉트 옵션 추가, 다수 정답을 모두 선택 시에만 정답 처리 |
| 3  | 답안 길이 조정 | 답안 길이를 유사하게 조정하여 시각적 균형 유지 | 각 답안을 비슷한 길이로 자동 조정하는 기능 |
| 4  | 토픽/주제 문맥 제공 | 주제에 맞는 추가 문맥과 예를 자동으로 제공 | 선택한 토픽에 따른 관련 문맥과 예시 자동 생성 기능 |
| 5  | 기출문제 기반 문제 생성 | 기출문제를 기반으로 새 문제를 생성하는 기능 | 사서 자격증시험, 토익, 토플 등의 기출문제를 활용한 문제 생성 기능 |
| 6  | 문제 난이도 조절 | 문제 난이도를 1부터 5까지 유연하게 조절 | 난이도 선택 시 실제 문제 생성에 반영 |
| 7  | 주관식 채점 및 수정된 답안 제시 | 주관식 문제 채점 시 수정된 답안을 제시 | 사용자가 입력한 답안을 바탕으로 모범 답안을 자동 생성하여 제시 |
| 8  | 변형 문제 생성 | 동일한 내용을 묻지만 다른 용어로 변형된 문제 생성 | 기존 문제와 유사한 문제를 변형하여 자동 출제 |
| 9  | 개인별 문제 풀이 기록 및 분석 | 개인별 문제 풀이 기록을 남기고, 부족한 부분을 확인 | 문제 풀이 기록 저장 및 분석을 통한 맞춤형 문제 추천 |
| 10 | 잘못된 문제 필터링 | LLM을 활용해 틀린 답을 가진 문제를 자동으로 폐기 | 문제를 풀어보고, 틀린 답을 가진 문제를 자동으로 폐기하고 새 문제 생성 |
| 11 | 각 문제 출제 소스별 예시 제공 | 각 문제의 출제 소스에 따라 예시가 입력박스 안에 포함되도록 | PDF, URL, YouTube 등 소스에서 예시 추출 후 입력박스에 표시 |
| 12 | 영어 문제 출제 | 영어 소스를 기반으로 영어 문제를 출제 | 영어로 된 문제 생성 및 예시 제공 기능 |
| __13__ | 콘텐츠 필터링 및 문자열 출력 | PDF, URL, YouTube 등의 내용을 필터링하여 필요한 부분만 출력 | 추출한 내용은 `page_content="..."` 형식으로 문자열만 출력 |
| 14 | YouTube 콘텐츠 편집 | YouTube 링크의 내용을 확인하고 클릭하여 편집 가능 | YouTube 내용 확인 후 수정 버튼 제공 및 자동 편집 기능 |


# 프로젝트 현황판
https://youtu.be/iT9Mi1pRvdg?si=nBag3GvG3WyEvZ8z
[토큰갯수링크](https://platform.openai.com/docs/models/gpt-3-5-turbo)

|     | 객관식 | 주관식 | 참/거짓 | 빈칸 | 한글 | 비고 |
|-----|-----|------|-----|----|----|----|
| 주제  |  o  |   o  |  o  | x  | o |   |
| 텍스트 |  o |  o   |  o  | x  | o | 기능추가  |
| 이미지 |  x  |  o   |  x  | x  | o | 기능추가  |
| pdf  |  o  |  o   |  o  |  △  | o |  |
| 유튜브 | o  | x  | x | x |o| 10분내외  |
| 영상  | x  |  x  | x  |x | x    | |

# 문제 유형별 최적화 된 프롬프트
## 주관식 Short answer
> * 1. ___Create short questions and answers, and translate korean, only prints korean.___
> * 시험자 : 신현수
> * 결과 :  Q: CROSS JOIN은 무엇을 의미하나요? _A: 두 테이블의 모든 행이 서로 한 번씩 조인되는 것을 의미합니다._  Q: FULL OUTER JOIN은 언제 사용되나요? _A: 두 테이블 중 하나에 있는 데이터가 다른 테이블에 없어도 모두 포함시키고 싶을 때 사용됩니다._  Q: RIGHT OUTER JOIN과 LEFT OUTER JOIN의 차이는 무엇인가요? _A: RIGHT OUTER JOIN은 오른쪽 테이블의 모든 행을 포함시키는 반면, LEFT OUTER JOIN은 왼쪽 테이블의 모든 행을 포함시킵니다._
> * 의견 : 문제와 답이 개념에 맞게 생성됨.
---

## 객관식 MCQ(multiple-choice problem)
> *  1. Create a quiz based on the context of {content}. 
   Include a variety of question types such as multiple choice, true/false, and short answer
   to test the participants understanding and knowledge depth.
   Put the answer at the end of each quiz. After finishing to generate quizes, translate them into Korean for print.
> * 작성자 : 지준 교수님.
> * 시험자 : 신현수
> * 결과 : I can't create quiz base on given concept.
> * 의견 : 프롬프트 메세지 길이와 생성물의 길이는 반비례 하는 것으로 보임.
> * 2. ___Create multiple-choice questions and answers, and translate korean, only prints korean.___
> * 시험자 : 신현수
> * 결과 : 쿼리문에서 사용되는 JOIN에 관한 다음 설명 중 옳은 것을 고르세요.
> CROSS JOIN은 두 테이블의 모든 행이 서로 한번씩 조인되는 방식이다.
> LEFT OUTER JOIN은 첫 번째 테이블의 모든 행과 두 번째 테이블의 일치하는 행이 조인된다.
> INNER JOIN은 한 테이블의 모든 행과 다른 테이블의 일치하는 행이 조인된다.
> RIGHT OUTER JOIN은 두 테이블의 모든 행이 서로 한번씩 조인되는 방식이다.
> 정답: 1. CROSS JOIN은 두 테이블의 모든 행이 서로 한번씩 조인되는 방식이다.
> * 의견 : 정답인 1번을 제외한 나머지 보기들은 잘못된 설명으로 옳게 생성됨.
---
## 참 거짓 True/False
> * Create true of false questions and answers, and translate korean, only prints korean.
> * 시험자 : 신현수
> * 결과 : 인덱스는 SQL문을 이용하여 생성할 수 있다. (True), CREATE UNIQUE INDEX는 중복이 없는 컬럼에 사용된다. (True), 뷰는 테이블과 같이 물리적 데이터를 갖는다. (False), 뷰를 통해 뷰 밖의 정보를 검색하는 것은 가능하다. (False), 인덱스의 역할은 정보를 빠르게 찾기 위한 것이다. (True)
> * 의견 : 참 거짓이 모두 맞게 생성됨.
---

## 빈칸 Blank
> * 1. Create fill-in-the-blank questions and answers, and translate korean, only prints korean. The blanks should represent missing words or phrases in the questions, to be filled in by the reader.
> * 시험자 : 신현수
> * 결과 : 인덱스를 생성하는 SQL문의 구문은 CREATE [UNIQUE] INDEX 인덱스이름ON 테이블명 (컬럼명) ; 이다. 인덱스이름은 ___________ 에서 지정한다. <br> CREATE INDEX 와 CREATE UNIQUE INDEX의 차이점은 무엇인가? CREATE INDEX는 중복된 값이 저장되는 컬럼에 사용되고, CREATE UNIQUE INDEX는 중복이 없는 컬럼에 사용된다. UNIQUE INDEX가 검색 성능이 더 좋다고 알려져 있다. <br> DBMS에서 대부분의 기본키 컬럼에 대해 자동으로 생성되고 사용되는 인덱스는 무엇인가? 기본키에 자동으로 설정된 ___________ 인덱스이다. <br> 인덱스를 생성하는 방법 중 하나로 SQL Developer의 GUI를 이용하는 방법에는 어떤 단계들이 포함되어 있는가? 접속창에서 인덱스 항목을 선택 후 [새인덱스]를 선택하고, 인덱스 편집화면에서 이름, 테이블, 인덱스 유형, 표현식을 입력해야 한다. 순차탐색(sequential search) 방법은 어떤 방식으로 동작하는가? 이름이 '___'인 튜플이 발견될 때까지 첫번째 튜플부터 차례로 비교하여 검색을 계속한다. 이는 간단한 방법이지만 검색 속도가 느리다.
> * 의견 : llm 이 답을 포함하라는 말을 이해를 잘 못함. 추가 실험 요망.


---
## 단기 목적
> * UI 만들기
> * 벤치마킹할 사이트 결정하기
> * 랭체인 아웃풋 parser (json, html 로 만드는 것 (chekcbox
> * 한글 유튜브 영상 (청크 사용)
> * 한글 pdf 로부터 객관식 문제 풀이 ( gpt4사용)
# 프로젝트 개요
* 문제 출제자의 편의를 돕기 위한 문제 생성기입니다.
* 학습자도 본인의 학업 성취도를 평가하기 위하여 사용할 수 있습니다.
* [직접 해보기](https://hsu-quizgen.streamlit.app)
* ![ezgif-3-57ad839840](https://github.com/ShinHyun-soo/QuizGen/assets/69250097/b9e538bc-a675-4125-a4b0-8d96f60725dc)
# Runs
```python
streamlit run Home.py
```
# Requirements
* langchain==0.1.13
* PyPDF2==3.0.1
* python-dotenv==1.0.0
* streamlit==1.33
* openai==1.23.6
* faiss-cpu==1.7.4
* altair==4
* tiktoken==0.5.2
* langchain-openai == 0.1.4
* transformers == 4.29.2
* pillow == 10.3.0

