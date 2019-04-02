import numpy as np
# 차수가 같을때
# a = np.arange(3)
# b = np.arange(3)
# c = a + b   #Vector Operation
# print(a)
# print(b)
# print(c)

# 차수가 같지 않을떄
# 결과 : ValueError: operands could not be broadcast together with shapes (3,) (6,)

# 5개의 배열을 서로 덧셈을 실행해 봅니다.
a = np.arange(3)    #[0 1 2]
b = np.arange(6)    #[0 1 2 3 4 5]
c = np.arange(3).reshape(-1,3)  #[[0 1 2]]
d = np.arange(6).reshape(-1,3)  #[[0 1 2]
                                #[3 4 5]]
e = np.arange(3).reshape(3,-1)  #[[0]
                                #[1]
                                #[2]]
# print(c+d)    # [[0 2 4]
                #  [3 5 7]]
# print(c+e)    #  [[0 1 2]
                #  [1 2 3]
                #  [2 3 4]]
# print(d+e)    # error

