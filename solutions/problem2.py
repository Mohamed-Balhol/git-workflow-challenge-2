# Problem 2: حساب مساحة المستطيل

try:
    length = float(input("أدخل طول المستطيل: "))
    width = float(input("أدخل عرض المستطيل: "))

    if length <= 0 or width <= 0:
        print("الرجاء إدخال أرقام موجبة وأكبر من الصفر للطول والعرض.")
    else:
        area = length * width
        print(f"\nمساحة المستطيل هي: {area}")
except ValueError:
    print("إدخال خاطئ! الرجاء إدخال أرقام صحيحة أو عشرية فقط.")