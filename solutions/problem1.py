
# Problem 1: العد التنازلي

try:
    num = int(input("أدخل رقماً صحيحاً: "))
    if num < 0:
        print("الرجاء إدخال رقم صحيح أكبر من أو يساوي الصفر.")
    else:
        print(f"\nالعد التنازلي من {num} إلى 0:")
        for i in range(num, -1, -1):
            print(i)
except ValueError:
 print("إدخال خاطئ! الرجاء إدخال رقم صحيح.")
 