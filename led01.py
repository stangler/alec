# LED 点灯

# 必要なモジュールを宣言
import RPi.GPIO as GPIO # GPIO を利用する

PNO = 4   # 対象の GPIO ポート番号
#PNO = 7  # 対象の GPIO ピン番号


# GPIO の初期化
GPIO.setmode(GPIO.BCM)    # BCM モード（ポート番号で指定する方法）
#GPIO.setmode(GPIO.BOARD) # BCM モード（ピン番号で指定する方法）
GPIO.setup(PNO, GPIO.OUT) # 指定した番号を out に設定

# 点灯
GPIO.output(PNO, GPIO.HIGH)
#GPIO.output(PNO, True)

# 消灯
#GPIO.output(PNO, GPIO.LOW)
#GPIO.output(PNO, False)


#GPIO.cleanup()

