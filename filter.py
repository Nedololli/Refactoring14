from PIL import Image
import numpy as np


def sumColor():
    global n, n1, sum_color
    for n in range(i, i + size):
        sum_color += np.sum(arr[n][j:j+size][:])
    sum_color //= 100

def grayColor():
    global n, n1
    for n in range(i, i + size):
        arr[n][j:j+size][:] = int(sum_color // 50) * 50 // gray



UrlImage = input(" укажите название файла, файл должен находится в корне. >> ")
UrlImage = UrlImage + ".jpg"
img = Image.open(UrlImage)
arr = np.array(img)
size = int(input("Введите размер ячейки >> "))

while True:
    try:
        switch = input(" Введите режим градации серого (4/6) >> ")
        if(switch == "4" or switch == "6"):
            gray = int(switch)
            break
        raise("Только 4/6")
    except:
        print("Только 4/6")
lenght_pic = len(arr)
i = 0



while i < lenght_pic - 1:
    j = 0
    while j < lenght_pic - 1:
        sum_color = 0
        sumColor()
        grayColor()
        j = j + size
    i = i + size
res = Image.fromarray(arr)
res.save('res.jpg')
