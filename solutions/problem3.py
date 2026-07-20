# Problem 3: الحاسبة البسيطة

try:
    num1 = float(input("أدخل الرقم الأول: "))
    num2 = float(input("أدخل الرقم الثاني: "))
    operation = input("اختر العملية الحسابية (+, -, *, /): ").strip()

    if operation == '+':
        result = num1 + num2
        print(f"\nالنتيجة: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"\nالنتيجة: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"\nالنتيجة: {num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("\nتحذير: لا يمكن القسمة على الصفر!")
        else:
            result = num1 / num2
            print(f"\nالنتيجة: {num1} / {num2} = {result}")
    else:
        print("\nعملية غير صالحة! الرجاء اختيار إحدى العمليات (+, -, *, /).")

except ValueError:
    print("\nإدخال خاطئ! الرجاء إدخال أرقام صحيحة أو عشرية فقط.")