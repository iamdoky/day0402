import numpy as np

a = [1,2,3,4,5]
b = [1.0,2.0,3.0,4.5,5.5]
c = ['a','b','c','d','e']
d = ['hello','java','python','oracle','mongo']
e = ['김경민','오상훈','이성기','김도희','정연미']
f = ['김','이순신은 거북선이 싫다고 하셨어 야이야이야','a','c','hello','hi']

arr1 = np.array(a)
arr2 = np.array(b)
arr3 = np.array(c)
arr4 = np.array(d)
arr5 = np.array(e)
arr6 = np.array(f)

print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)
print(arr4.dtype)
print(arr5.dtype)
print(arr6.dtype)

print(arr1.shape)   # 차수와 데이터 수를 확인 (5,)
print(arr1.ndim)    # 차수만 확인            1
print(arr1.dtype)   # 요소하나를 위한 자료형  int32

# 요소에 따라서 데이터 크기가 달라진다. 유니코드 + 데이터 사이즈