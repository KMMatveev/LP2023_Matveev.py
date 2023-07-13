import struct
import time
import numpy as np
from serial import Serial, EIGHTBITS, PARITY_NONE, STOPBITS_ONE
import threading
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets

#f = open('data.txt', 'w')
# Создаем окно и график
win = pg.GraphicsLayoutWidget(show=True)
plot = win.addPlot()
curve = plot.plot(pen='y')

# Начальные данные
data2 = np.zeros(1000)

def update():
    global data2
    # Считываем данные из списка data
    temp_c = data1[-1]
    # Добавляем новые данные в data
    data2[:-1] = data2[1:]
    data2[-1] = temp_c
    # Обновляем данные графика
    curve.setData(data2)

def update_data():
    global data1
    data1 = []
    data1.append(0)
    #k = 0
    while True:
        s.write(b'0')
        data = s.read(2)
        #print(data)
        try:
            d = struct.unpack("H" * 1, data)
            #d = (random() * 4000) // 1 #случайные данные для проверки работы графика без подключения микроконтроллера
            data1.append(d[0])
            #f.write(f'{d[0]}\n')
            #print('=====')
            #print(d)
            #k += 1
            #if k == 10:
                #print(time.time() - start_time)
                #break
            #print(' ')
        except:
            print('-----')
            continue

Thread_Alive = True
iterator = 0
number = 1024

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0.0001)
if __name__ == '__main__':
    print("start")
    s = Serial(port="COM4", baudrate=115200, bytesize=EIGHTBITS, parity=PARITY_NONE, stopbits=STOPBITS_ONE, timeout=1)
    time.sleep(0.3)
    print("found")

    try:
        start_time = time.time()
        data_thread = threading.Thread(target=update_data)
        data_thread.start()
        QtWidgets.QApplication.instance().exec()
        #f.close()
    except KeyboardInterrupt:
        #f.close()
        print("Exit")
        pass