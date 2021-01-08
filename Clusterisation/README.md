Тема: Кластеризация
===================

Отчет.
------

### Постановка задачи:

Необходимо разбить набор точек на плоскости на кластеры. Известно, что
расстояние между кластерами не превышает некоторое расстояние.\
Надо сначала провести иерархическую кластеризацию на малой выборке,
потом - k-means

### Формат входных и выходных данных:

Ввод: файл. Каждая строка -- координаты точки. Набор данных генерируется
случайно с заранее известным распределением.

Вывод: изображение изначального набора данных, предварительных кластеров
после иерархической кластеризации и окончательных кластеров после
применения метода k-means

### Краткое описание метода:

Сначала из набора данных случайным образом выбирается 500 точек. На них
проводится иерархическая кластеризация, и получаются прототипы итоговых
кластеров. Центры прототипов кластеров выбираются для старта метода
k-means.

### Замечание:

Метод k-means делит пространство на области Вороного с центрами в
центрах кластеров и не может быть использован, если точки делятся на
кластеры более сложным образом.

### Примеры работы программы:

![image002](https://user-images.githubusercontent.com/74815433/104017978-215e3d80-51ca-11eb-916b-38d56ce7ffbb.jpg)

![image004](https://user-images.githubusercontent.com/74815433/104017984-23280100-51ca-11eb-9ad0-12b61bb2cca7.jpg)

![image006](https://user-images.githubusercontent.com/74815433/104017987-24f1c480-51ca-11eb-8168-2eda451a40aa.jpg)


### Вывод:

Как видно из примеров, метод k-means работает далеко не всегда. Кроме
того, при фиксированном минимальном расстоянии между кластерами и
неизвестном количестве кластеров предварительных кластеров может
оказаться значительно больше, чем должно быть.