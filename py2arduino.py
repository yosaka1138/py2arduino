"""
 ___   _                        _                        _ 
|_ _| | |    _____   _____     / \   ___ _   _ _ __ ___ (_)
 | |  | |   / _ \ \ / / _ \   / _ \ / __| | | | '_ ` _ \| |
 | |  | |__| (_) \ V /  __/  / ___ \\__ \ |_| | | | | | | |
|___| |_____\___/ \_/ \___| /_/   \_\___/\__,_|_| |_| |_|_|
                                                           
 _  __                 
| |/ /__ _ _ __   __ _ 
| ' // _` | '_ \ / _` |
| . \ (_| | | | | (_| |
|_|\_\__,_|_| |_|\__,_|

"""
#coding: utf-8
from time import sleep
from pyfirmata2 import Arduino, util

class set_pin():
    def __init__(self, board, pin, mode, data):
        """
        board: Arduino()
        pin: アナログ/デジタルピン番号
        mode: input / output / pwm
        data: analog / digital 
        """
        self.board = board
        self.pin = pin
        self.mode = mode
        self.data = data
        self.sampling_rate = 100    # 50 Hz
        self.socket = self.board.get_pin("{}:{}:{}".format(self.data[0], self.pin, self.mode[0]))
        if self.mode == "input":
            self.socket.enable_reporting()
    
    def analogread(self):
        analog_value = self.socket.read()
        if analog_value == None:
            pass
        else:
            casted_value = int(analog_value * 1024)
            return casted_value

    def read(self):
        if self.data[0] == "a":
            analog_value = self.socket.read()
            if analog_value == None:
                pass
            else:
                casted_value = int(analog_value * 1024)
                return casted_value
        elif self.data[0] == "d":
            return self.socket.read()

    def pwm(self, value):
        # 多分PWM用になりそう
        self.socket.write(value)

    def high(self):
        self.socket.write(1)

    def low(self):
        self.socket.write(0)