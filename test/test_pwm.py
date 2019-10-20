#coding: utf-8
"""
デジタルピンに刺したLEDをPWM制御する
"""
import time
import math
from pyfirmata2 import Arduino
from py2arduino import set_pin

def main():
    # 操作するArduinoを決定
    board = Arduino(Arduino.AUTODETECT)
    # pwm_0をデジタルピンのoutputに設定
    pwm_0 = set_pin(board, pin=10, mode="pwm", data="digital")
    dt = 0.1
    while True:
        # LEDを点灯
        pwm_0.pwm((math.sin(math.pi*dt)+1.0)/2)
        time.sleep(0.05)
        dt += 0.1
        # dt増やしてくとメモリが怖いので１周したら0に戻す
        if dt == 2.0:
            dt = 0.0

if __name__ == "__main__":
    main()