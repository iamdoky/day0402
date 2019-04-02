import numpy as np

a = np.arange(3)
print(a)
print(a+1)  # BroadCasting
print(a>1)  # BroadCasting
print(a[a>1])   # 배열의 1번쨰 보다 큰수를 출력 / true인 녀석을 출력.

b = np.arange(6).reshape(-1,3)
bb = np.arange(6).reshape(2,-1)
bbb = np.arange(6).reshape(2,3)
print(b)
print(bb)
print(bbb)
print(b+1)
print(b>1)  # 브로드캐스팅 b의 요소만큼 비교하여 True,False를 반환
print(b[b>1]) # 브로드캐스팅의 True 요소만 출력
print(b[0])
print(b[0][0])
print(b[1])