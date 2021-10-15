import numpy as np
import matplotlib.pyplot as plt
array = []

def langr(x, y, n):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1

        for i in range(len(x)):
            if i==j:
                p1 = p1 * 1; p2 = p2 * 1
            else:
                p1 = p1 * (n - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z


# Определяемся с количеством вывода графиков
def num_of_graph(arr):
    print(f"Графиков в файле: {len(arr)} Сколько графиков вывести?\n")
    quantity = list(
        map(
            int,
            input(
                f"Примеры возможных значений: 1 2 3 (для вывода нескольких графиков), 3 (для конкретного). Для вывода всех графиков, введите: 0) \n")
                .split(' ')
        )
    )
    # Слушаем введенный запрос
    if len(quantity) == 1:
        return arr if quantity[0] == 0 else [arr[quantity[0] - 1]] 

    elif len(quantity) > 1:
        i = 0
        points_arr = []
        while (i < len(quantity)):
            points_arr.append(arr[quantity[0 + i] - 1])
            i = i + 1
        return points_arr

    else:
        return "Указано некорректное значение графиков"


def draw(points):
    for point in points:
        print(point)
        x = point[0]
        y = point[1]
        plt.scatter(x, y)
    plt.title("Графики")
    plt.show()

def howdraw(res):
        num =  int(input(f"1 - полиномом Лагранжа, 0 - просто вывести точки.\n"))
        if num == 1:
            for graph in res:
                x = graph[0]
                y = graph[1]
                x.sort()
                y.sort()
                plt.scatter(x, y)
                xnew = np.linspace(np.min(x), np.max(x), 50)
                ynew = [langr(x, y, i) for i in xnew]
                plt.plot(xnew, ynew)
            plt.title("Полином Лагранджа")
            plt.show()
        
        else:
            for point in res:
                x = point[0]
                y = point[1]
                plt.scatter(x, y)
            plt.title("Графики")
            plt.show()
            


with open('points.txt', 'r') as f:
    for line in f.read().split('\n'):
        new_line = line[1:-1].split(']&&[')
        a = [list(map(float, elem.split(','))) for elem in new_line]
        array.append(a)

res = num_of_graph(array)
howdraw(res)
