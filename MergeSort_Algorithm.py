def merge(arr, front, mid, end):
    left = arr[front:mid+1]
    right = arr[mid+1:end+1]
    # print('front is ', front)
    # print('end is ', end)
    # print('mid is ', mid)
    # print("left: ", left)
    # print("right: ", right)
    i = j = 0
    index = front
    while (i < len(left)) and (j < len(right)):
        # print("i = ", i)
        # print("j = ", j)
        if left[i] < right[j]:
            arr[index] = left[i]
            i += 1
        else:
            arr[index] = right[j]
            j += 1
        index += 1
    while i < len(left):
        arr[index] = left[i]
        i += 1
        index += 1
    while j < len(right):
        arr[index] = right[j]
        j += 1
        index += 1
    print(" ".join(str(i) for i in arr[front:index]))


def merge_sort(arr, front, end):
    if front < end:
        mid = (front+end)//2
        merge_sort(arr, front, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, front, mid, end)
    elif front == end:
        print(arr[front])


arr_num = input("欲排列數字個數：")
target_arr = input("輸入欲排列數字(以空白鍵分隔)：").split(' ')
target_arr = list(map(int, target_arr))
merge_sort(target_arr, 0, int(arr_num)-1)
