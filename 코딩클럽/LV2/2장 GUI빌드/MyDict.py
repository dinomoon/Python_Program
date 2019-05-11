from tkinter import *

# 키 입력 함수
def click():
    entered_text = entry.get()  # 텍스트 엔트리 위젯에서 사용자가 입력한 텍스트를 가져와 entered_text에 저장함
    output.delete(0.0, END)  # 텍스트 박스의 내용을 지움
    definition = my_dict[entered_text]  # 사전에서 정의를 가져와서 definition에 저장함
    output.insert(END, definition)  # 텍스트 박스에 정의를 넣음

#### 메인
window = Tk()
window.title("MyDict")

# 레이블 생성
Label(window, text = "정의되어 있는 단어를 입력하고 엔터 키를 누르세요: ").grid(row = 0, column = 0, sticky = W)

# 텍스트 엔트리 위젯 생성
entry = Entry(window, width = 20, bg = "light green")
entry.grid(row = 1, column = 0, sticky = W)

# 제출 버튼 추가
Button(window, text = "제출", width = 5, command = click).grid(row = 2, column = 0, sticky = W)

# 다른 레이블 생성
Label(window, text = "\n정의").grid(row = 3, column = 0, sticky = W)

# 텍스트 박스 생성
output = Text(window, width = 75, height = 6, wrap = WORD, background = "lightgreen")
output.grid(row = 4, column = 0, sticky = W)

# 사전
my_dict = {
    '알고리즘': '컴퓨터로 작업을 수행하기 위해 컴퓨터가 이해할 수 있도록 단계별로 설명해놓은 것',
    '2진법': '2진법으로 나타낸 숫자'
}

#### 메인 반복문 실행
window.mainloop()