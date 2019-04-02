import numpy as np

# a = np.zeros(3) # 초기값을 0으로 체움; 제로스
# print(a)
#
# b = np.ones(10)
# print(b)

# a = np.zeros([3,4], dtype=int)
# print(a)

a = np.arange(12).reshape(-1,4)

# a배열과 동일한 shape의 배열을 생성 0으로 채움
b= np.zeros_like(a)
c = np.zeros(a.shape, dtype=int)
print(b)
print(c)

# print(a)
# print()
# print(np.sum(a, axis=0))    # 행의 합
# print()
# print(np.sum(a, axis=1))    # 열의 합
# print()
# print(np.max(a, axis=1))    # 열의 합
# print()
# print(np.max(a, axis=1))    # 열의 합