import numpy as np

a = [[1,2,3],[4,5,6],[[1,2,3,],[4,5,6]]]
arr = np.array(a)
arr2= np.flatiter(a)
print(arr)
print(arr2)




# 점수가 가장 높은 학생의 이름을 출력 / 동점인 사람도 출력
# name = ['원진아','슬기','이솜','청하','박주호','김경민','김태리']
# score = [100,100,96,88,91,18,100]
# n = np.array(name)
# s = np.array(score)
# m = max(score)
# sc = np.argmax(score)
# w = np.argwhere(score == np.max(score))
# # w = w.reshape(1,3)[0]
# print(w)
# print(n[w])
#

# winner = np.argwhere(listy == np.amax(listy))

# 연습) a배열의 요소만큼의 행의 크기를 갖고 열은 a배열의
# 요소중에 최대값의 열의 크기를 갖는 2차원 배열을 만들고고a = [1,3,0,3,1]
# a = [1,3,0,3,1]
# b = np.eye(len(a),np.max(a)+1,dtype=int)[a]
# print(b)
# a = [4,3,1,5,2,5,5,5,5]
# arr1 = np.array(a)
# print(arr1)
# max1 = np.max(arr1)
# idx = np.argmax(arr1)
# print(max1)
# print(idx)

# 성적순으로 이름을 출력하여 봅니다.
# name = ['슬기','이솜','청하','주호','경민','태리','재인']
# score = [100,96,88,100,18,95,99]
#
# # s = np.argsort(score)
# s = np.argsort(score)[::-1]
# n = np.array(name)
# print(s)
# print(n[s])
# print('-----------------------------------------------------------')
#
# n1 = np.array(name)
# s1 = np.array(score)
#
# arr = np.argsort(s1)[::-1]
# print(arr)
# print(n1[arr])


#  정렬 시 인덱스 값가져오기
# a = [4,3,1,5,2]
# arr1 = np.array(a)  # 넘파이 배열
# b = np.argsort(arr1)
# print(a)
# print(b)
# print(arr1[b])

# b = np.zeros([len(a),np.max(a)+1],dtype=int)
# b[[range(len(a))],a] = 1
# print(b)

# a = np.eye(5,5, dtype=int)
# print(a)

#a = np.zeros([5,5],dtype=int)









# arr = np.zeros([5, 5], dtype='int32')
# for i in range(5):
#     arr[i, i] = 1
#
# print(arr)

# a = np.arange(25).reshape(5,5)
#
# b = np.ones([5,5],dtype=int)
# b[1:-1,1:-1] = 0
# print(b)
# print(a)
# print(a>5)
# print(a[a>5])   # bool Array
# print('-------------------')
# print(a[0,1])   # 0번째 행의 1번째 열 ( a[행,열] )
# print(a[1,0])   # 1번째행, 0번째행    index Array
# print(a[[1,0],[0,1]])   #[행 행], [열 열] [1행 0행],[0열 1열]   index Array
# print('-------------------')
# a[[1,0],[0,1]] = 100
# print(a)
#
# b = np.zeros([5,5], dtype=int)
# b[:,[0,-1]] = 1
# b[[0,-1]] = 1
# print(b)
