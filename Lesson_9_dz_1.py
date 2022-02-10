import time


class TrafficLight:

    def running(self):
        self.__color = "Красный"
        print(f"Загорелся {self.__color} сигнал светофора")
        time.sleep(7)
        self.__color = "Желтый"
        print(f"Загорелся {self.__color} сигнал светофора")
        time.sleep(2)
        self.__color = "Зелёный"
        print(f"Загорелся {self.__color} сигнал светофора")
        time.sleep(9)


a = TrafficLight()
a.running()
