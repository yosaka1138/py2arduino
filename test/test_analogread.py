#coding: utf-8
"""
アナログピンに刺したセンサから取得した値を表示する
"""
import time
from pyfirmata2 import Arduino
from py2arduino import set_pin

def main():
    # 操作するArduinoを決定
    board = Arduino(Arduino.AUTODETECT)
    # サンプリング周期を10msに固定
    board.samplingOn(10)
    # pin1 をアナログピンのinputに設定
    analog_0 = set_pin(board, pin=0, mode="i", data="analog")
    time.sleep(2)
    while True:
        # センサから取得した値を0~1024(int)で出力
        print(analog_0.read())
        time.sleep(0.5)
    # アナログピンのサンプリングを終了する
    board.samplingOff()

if __name__ == "__main__":
    main()