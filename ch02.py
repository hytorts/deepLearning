# AND 게이트 구현
# def AND(x1, x2):
#     w1, w2, theta = 0.5, 0.5, 0.7
#     tmp = x1 * w1 + x2 * w2
#     if tmp <= theta:
#         return 0
#     elif tmp > theta:
#         return 1
    
# print(AND(0, 0)) # 0
# print(AND(1, 0)) # 0
# print(AND(0, 1)) # 0
# print(AND(1, 1)) # 1

# numpy 사용
# import numpy as np
# x = np.array([0, 1]) # 입력
# w = np.array([0.5, 0.5]) # 가중치
# b = -0.7 # 편향

# print(w * x) # [0.  0.5]
# print(np.sum(w * x)) # 0.5
# print(np.sum(w * x) + b) # -0.19999999999999996 대략 -0.2(부동소수점 수에 의한 연산 오차)

# 가중치와 편향을 도입한 AND 게이트
# import numpy as np
# def AND(x1, x2):
#     x = np.array([x1, x2])
#     w = np.array([0.5, 0.5])
#     b = -0.7
#     tmp = np.sum(w * x) + b
#     if tmp <= 0:
#         return 0
#     else:
#         return 1
    
# print(AND(0, 0)) # 0
# print(AND(1, 0)) # 0
# print(AND(0, 1)) # 0
# print(AND(1, 1)) # 1

# 가중치와 편향을 도입한 NAND 게이트
# import numpy as np
# def NAND(x1, x2):
#     x = np.array([x1, x2])
#     w = np.array([-0.5, -0.5]) # AND와는 가중치(w와 b)만 다르다
#     b = 0.7
#     tmp = np.sum(w * x) + b
#     if tmp <= 0:
#         return 0
#     else:
#         return 1

# print(NAND(0, 0)) # 1
# print(NAND(1, 0)) # 1
# print(NAND(0, 1)) # 1
# print(NAND(1, 1)) # 0

# 가중치와 편향을 도입한 OR 게이트
# import numpy as np
# def OR(x1, x2):
#     x = np.array([x1, x2])
#     w = np.array([0.5, 0.5]) # AND와는 가중치(w와 b)만 다르다
#     b = -0.2
#     tmp = np.sum(w * x) + b
#     if tmp <= 0:
#         return 0
#     else:
#         return 1

# print(OR(0, 0)) # 0
# print(OR(1, 0)) # 1
# print(OR(0, 1)) # 1
# print(OR(1, 1)) # 1

# XOR 게이트 구현
import numpy as np
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5]) # AND와는 가중치(w와 b)만 다르다
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) # AND와는 가중치(w와 b)만 다르다
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print(XOR(0, 0)) # 0
print(XOR(1, 0)) # 1
print(XOR(0, 1)) # 1
print(XOR(1, 1)) # 0