import numpy as np

a = [0,1,2,3,4,5]
arr = np.array(a)
print(arr)

arr2 = arr.reshape(2,3)
print(arr2)

print(arr.shape)    # shape 차수를 확인
print(arr2.shape)

print(arr.ndim)     # ndim 차수를 확인
print(arr2.ndim)

print(arr.dtype)    # 차수안에 값의 타입.
print(arr2.dtype)

# b = np.arange(5)
#
# c = np.array(a)
# print(c)
# print(type(c))