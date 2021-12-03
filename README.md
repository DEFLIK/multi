# Отчет
Перед началом всех измерений зафиксируем работу компьютера в обычном состоянии,
а также запишем ссылки в текстовый документ с помощью io_bound_init_urls.py
![clear](assets/graphClear.png)

# IO-bound
## IO-bound sync
Замерим время синхронной проверки ссылок через io_bound.py
Затраченное на это время составило около 23 минут
![io_1_t](assets/IOtime1t.png)

По отчёту можно понять, что пропускная способность синхронной работы
составила около 32 кбит/с на отправку запроса и 776 кбит/с на получение ответа
по интернету, остальные показатели значительно не изменились
![io_1_g](assets/IOgraph1t.png)

## IO-bound async 5 threads
Время асинхронной проверки ссылок через io_bound_threading.py при 5 рабочих потоках
составило около 5 минут, причём пропускная способность повысилась до 96 кбит/c отпр.
и 2.3 Мбит/с получ.
![io_5_t](assets/IOtime5t.png)
![io_5_g](assets/IOgraph5t.png)

## IO-bound async 10 threads
Асинхронная проверка при 10 потоках составила около 3 минут. Пропускная способность
200 кбит/c отп. 3.3 Мбит/с получ.
![io_10_t](assets/IOtime10t.png)
![io_10_g](assets/IOgraph10t.png)

## IO-bound async 100 threads
Асинхронная проверка при 100 потоках составила около 2 минут. Пропускная способность
360 кбит/c отп. 4.5 Мбит/с получ.
![io_100_t](assets/IOtime100t.png)
![io_100_g](assets/IOgraph100t.png)

## IO-bound вывод
По итогу можно понять, что при использовании ThreadPoolExecutor повышение кол-ва потоков, 
которые запрашивают данные по сети, понижает суммарное время ожидания всех ответов,
а также повышает общую пропускную способность запросов через интернет. 
Иные показатели особо не изменяются

# CPU-bound
## CPU-bound sync
Замерим скорость генерации монетки на 1 ядре с помощью cpu_bound.py
Врмя получения одной монетки составили около 1-2 минут
![cpu_1_t](assets/CPUtime1t.png)

Можно заметить, что процент загрузки процессора возрос до 20% (3% изнач.),
а скорость повысилась до 3.89ГГц (1.61ГГц изнач.)
![cpu_1_g](assets/CPUgraph1t.png)

## CPU-bound async 2 proc
Теперь попробуем повторить генерацию, но уже с двумя процессами 
с помощью cpu_bound_threading.py
Время генерации теперь составило также около 1-2 минут. Сам же процессор
теперь работает на 35%

![cpu_2_t](assets/CPUtime2t.png)
![cpu_2_g](assets/CPUgraph2t.png)

## CPU-bound async 4 proc
4 процесса, время ожидания значительно понизилось до 22 секунд,
процессор задействован на 60%

![cpu_4_t](assets/CPUtime4t.png)
![cpu_4_g](assets/CPUgraph4t.png)

## CPU-bound async 5 proc
5 процессов, время ожидания примерно 20 секунд,
процессор задействован на 74%

![cpu_5_t](assets/CPUtime5t.png)
![cpu_5_g](assets/CPUgraph5t.png)

P.S. Интересно заметить, что в некоторых случаях при работе с 5
потоками получилось получить монетку всего за 2 секунды, что указывает
на присутствие элемента удачи при генерации монеток

![cpu_5_t_2](assets/CPUtime5t-2.png)

## CPU-bound async 10 proc
При 10 процессах процессор задействует все свои ядра и работает
на 100% с максимальной скоростью. Итоговое время генерации монетки получилось
равным 9 секундам

![cpu_10_t](assets/CPUtime10t.png)
![cpu_10_g](assets/CPUgraph10t.png)

## CPU-bound async 61 proc
Поставим максимальное значение - 61 процесс, которое допускает ProcessPoolExecutor.
В итоге процессор также работает на 100% с максимальной скоростью. Итоговое время - 11 секунд
Видно, что ставить процессов больше, чем позволяет сам процессор не имеет смысла

![cpu_61_t](assets/CPUtime61t.png)
![cpu_61_g](assets/CPUgraph61t.png)

## CPU-bound вывод
По итогу можно сказать, что использовании ProcessPoolExecutor повышается процент использования
процессора (кол-во его ядер) и его скорость. Также было выявлено, что использование процессов
количеством больше, чем позволяет сам процессор не имеет смысла