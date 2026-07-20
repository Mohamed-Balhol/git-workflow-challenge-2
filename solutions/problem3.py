N = int(input("أدخل قيمة N: "))

c = 0
b = 1
i = 0

while i < N:
    print(c , end=" ")
    next = c + b
    c = b
    b = next
    i += 1