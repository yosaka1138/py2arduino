# Py2Arduino

## 概要

pythonのモジュールであるpyfirmata2を用いてArduinoを動かすためのモジュールです。

| language or modules | version |
| :-----------------: | ------- |
|       python        | 3.x.x   |
|      pyfirmata      | 2.0.1   |

## 使い方

サンプルコードは[test](test)を参考にしてください。以下を試し、動作を確認しています。

- [Lチカ](test/test_digitalwrite.py)
- [センサの値の読み取り](test/test_analogread.py)
- [デジタルピンの読み取り](test/test_digitalread.py)
- [PWM(LED)](test/test_pwm.py)



以下の手順でこのライブラリが登録されます。

```bash
> cd py2arduino
> sudo pip3 install -e .
> sudo pip3 install -r requirements.txt
> sudo python3 setup.py develop
```



