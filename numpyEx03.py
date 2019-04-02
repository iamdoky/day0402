import numpy as np

# 다른 자료형으로 배열을 생성할 수 있다.
# 정수형의 파이썬 배열 ==> 실수형 numpy 배열 생성
# np.array(파이썬배열, dtype = 자료형)

a = [0,1,2,'3',4,5]               # '3' 변환가능
# a = [0,1,2,'하이',4,5]         '하이' 변환 불가
b = np.array(a, dtype=float)    # 정수를 실수로 변환
print(b)


