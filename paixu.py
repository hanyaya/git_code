#排序算法--冒泡
arr1 = [1,2,8,5,6,9,4]
for i in range(len(arr1))[::-1]:
	for j in range(i):
		if arr1[j]>arr1[j+1]:
			arr1[j],arr1[j+1] = arr1[j+1],arr1[j]
print(arr1)

#快速排序
#插入排序-将序列的第一个看成是有序序列，后面的元素逐个插入。
arr2 = [1,2,8,5,6,9,4]
# for i in range(1, len(arr2)):
#     key = arr2[i]
#     j = i - 1#保证j可以被索引
#     while j >= 0:
#         if arr2[j] > key:
#             arr2[j + 1] = arr2[j]
#             arr2[j] = key
#         j -= 1
# print(arr2)
for i in range(1,len(arr2)):#进行n-1趟
	while i-1 >=0:
		if arr2[i-1]>arr2[i]:
			arr2[i],arr2[i-1] = arr2[i-1],arr2[i]
		i -=1
print(arr2)
#直接选择排序
arr3 = [1,2,8,5,6,9,4]
for i in range(len(arr3)):
	mins = i
	for j in range(i+1,len(arr3)):
		if arr3[mins] > arr3[j]:
			mins = j
	arr3[mins],arr3[i] = arr3[i],arr3[mins]
print(arr3)
