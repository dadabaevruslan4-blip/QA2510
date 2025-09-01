# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_QA(name):
    print(f'Hi, {name}')



print_QA("Abai")
print(f'Hi')  # Press Ctrl+F8 to toggle the breakpoint.
print(f'Friday')


age = 28
if age < 18:
    print("Несовершеннолетний")
    print("Доступ ограничен")
elif age >= 18 and age < 65:
     print("Взрослый")
     print("Доступ разрешен")
else:
    print("Пенсионер")
    print("Специальный доступ")







for i in range(5):
    print(i) # Выведет числа от 0 до 4


fruits = ["яблоко", "банан", "апельсин"]
for i in fruits:
    print(i)


count = 0
while count < 10:
    print(count)
    count += 2 # Важно: не забывайте обновлять условие!





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Hello')
    print_QA("Ruslan")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
