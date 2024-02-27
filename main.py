from random import randint

def main():
    # вводим кол-во чисел
    n = input("Введите кол-во чисел: ")
    n = int(n)
    mas = []
    for i in range(n):
        mas.append(randint(1, 99))
    print('Исходный массив:', mas)
    i = 0
    #до предпоследнего числа
    while i < n-1:
        j = 0
        while j < n-1-i:
            #сравниваем 2 числа
            if mas[j] > mas[j+1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]
            j += 1
        i += 1
    print('Результат:', mas)


if __name__ == '__main__':
    main()