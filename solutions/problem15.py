arr = [8, 3, 6, 1, 9, 2]

n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("المصفوفة بعد الترتيب:")
print(arr)