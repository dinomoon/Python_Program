from tkinter import *

# 키 입력 함수
def click_Q():
    qestions = list(my_dict.keys())
    question_text.delete(0.0, END)
    question = my_dict[questions[0]]
    question_text.insert(END, question)


def click_A():
    pass

#### 메인
window = Tk()
window.title("My Flash Cards")

# 버튼 추가
Button(window, text = "질문 얻기", command = click_Q).grid(row = 0, column = 0, sticky = W)
Button(window, text = "답 얻기", command = click_A).grid(row = 0, column = 4, sticky = E)

# 질문 얻기 클릭하면 질문 생기는 텍스트 박스
question_text = Text(window, width = 20, bg = 'light green')
question_text.grid(row = 1, column = 0, sticky = W)

# 정의 레이블
Label(window, text = "\n정의:").grid(row = 2, column = 0, sticky = W)

# 결과 출력 텍스트 박스
output = Text(window, width = 20, height = 6, bg = "light green")
output.grid(row = 3, column = 0, sticky = W)

#### 메인 반복문 실행
window.mainloop()

# 사전
my_dict = {
    '알고리즘': '컴퓨터로 작업을 수행하기 위해 컴퓨터가 이해할 수 있도록 단계별로 설명해놓은 것',
    '2진법': '2진법으로 나타낸 숫자'
}