# Перший код - як вивести текст

#print("Hello World!")

# Другий код - змінна

#! Ім'я змінної не може містити в собі пробіли.
#! Ім'я змінної не може починатися з числа.
#! Регістр для змінних важливий, тобто є різниця між var і Var.

#first = 23
#print(first)

#-------------------------------------------------------------------
#second = "Number"
#print(second)

#-------------------------------------------------------------------
#print(first, "is a", second)

# Третій код - як проводити операції над числами.

#! Для того щоб поєднати дві змінні в одну (одного типу) використовується +.

#a_1 = 10 + 5
#b_1 = a_1 + 20
#c_1 = (a_1 + b_1) * 2
#print(a_1, b_1, c_1)

# Чевертий код - робота з рядками

#! Під час створення рядка, враховується тільки перші лапки.

#first_string = "Hello World!"
#second_string = 'Hello World!'
#third_string = """Hello World!"""

#-------------------------------------------------------------------

#name = input("Ваше ім'я? ")
#greeting = "Привіт, " + name
#print(greeting)

#-------------------------------------------------------------------

# Для того щоб вивести довжину слова використоємо len(змінна)
#string = input("Напишіть любий текст: ")
#string_length = len(string)
#print(string_length)

# Пятий код - типи данних, перетворення типів.

#! Для того щоб конвертувати любе значення любе значення в текст пишемо str(змінна).
#! Для того щоб конвертувати любе значення любе значення в число пишемо int(змінна).

#result_1 = 10 + 15
#text_1 = "Результат = " + str(result_1)
#print(text_1)

#-------------------------------------------------------------------

#result_2 = "10" + "15"
#text_2 = "Результат = " + (result_2)
#print(text_2)

#-------------------------------------------------------------------

#a_2 = input("Перше число: ")
#b_2 = input("Друге число: ")
#result_3 = int(a_2) + int(b_2)
#text_3 = "Результат = " + str(result_3)
#print(text_3)

# Шостий код - логічна перевірка if + elif + else

first_number = input("Перше число: ")
first_simbol = input("Перший cимвол (+ або -): ")
second_number = input("Друге число: ")
second_simbol = input("Другий символ (+ або -): ")
third_number = input("Третє число: ")

if first_simbol == "+":
    int(first_number) + int(second_number)
else: 
    print("Це не + або -!")

if first_simbol == "-":
    int(first_number) - int(second_number)
else: 
    print("Це не + або -!")

if second_simbol == "+":
    int(first_number) + int(first_simbol) + int(second_number) + int(third_number)
else: 
    print("Це не + або -!")

if second_simbol == "-":
    int(first_number) + first_simbol + int(second_number) - int(third_number)
else: 
    print("Це не + або -!")