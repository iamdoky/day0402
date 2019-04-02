import numpy as np

a = ['160.7','170.5','162.5','158.5','169.5','168.5','175.5','177.7','188.8','185.5']

# 연습) 파이썬 배열을 numpy 배열로 만든 후 170 이상인 데이터만 뽑아 새로운 numpy 배열을 만드시오

height = np.array(a,dtype=float)
h = height[height>170]
print(height)
print(h)