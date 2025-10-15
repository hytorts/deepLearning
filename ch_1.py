# 변수
animal = "turtle"
age = 10
print(animal)
print(age)

# 리스트
fruits = ["사과", "바나나", "포도"]
print(fruits[0])   # 사과

# 딕셔너리
animal = {"종": "turtle", "성별": "수컷", "이름": "꼬북이", "나이": 10}
print(animal["종"]) # turtle
print(animal["이름"]) # 꼬북이

# if문
animal = "turtle"

if animal == "turtle":
    print("거북이가 맞습니다.")
else:
    print("거북이가 아닙니다.")
    
# for문
for i in[1, 2, 3]:
    print(i)

# 함수
def hello():
    print("Hello World!")

hello() # Hello World!

def animal(object):
    print("Hello " + object + "!")

animal("turtle")

# 클래스
class animal:
    def __init__(self, name):
        self.name = name
        
    def hello(self):
        print("Hello " + self.name + "!")
        
    def goodby(self):
        print("Good-bye " + self.name + "!")

a = animal("turtle")
a.hello()
a.goodby()

# 넘파이 배열 생성
import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(x) # [1. 2. 3.]

# 넘파이 N차원 배열
A = np.array([[1, 2], [3, 4]])
print(A)
# [[1 2]
#  [3 4]]
print(A.shape) # (2, 2)
print(A.dtype) # int64

# 브로드캐스트
A = np.array([[1, 2], [3, 4]])
B =  np.array([10, 20])
print(A * B)

#[[10 40]
# [30 80]]

# 단순 그래프 그리기
import matplotlib.pyplot as plt

#데이터 준비
# x = np.arange(0, 6, 0.1) # 0에서 6까지 0.1 간격으로 생성
# y = np.sin(x)

# # 그래프 그리기
# plt.plot(x, y)
# plt.show()

# pyplot의 기능
# x = np.arange(0, 6, 0.1) # 0에서 6까지 0.1 간격으로 생성
# y1 = np.sin(x)
# y2 = np.cos(x)

# #그래프 그리기
# plt.plot(x, y1, label="sin")
# plt.plot(x, y2, linestyle="--", label="cos") # cos 함수는 점선
# plt.xlabel("x") # x축 이름
# plt.ylabel("y") # y축 이름
# plt.title("sin & cos") # 제목
# plt.legend()
# plt.show()

# 이미지 표시
from matplotlib.image import imread

img = imread('ch1.png') # 이미지 읽어오기(경로 설정)

plt.imshow(img)
plt.show()