#!/usr/bin/python 
# coding:utf-8 
 
#timeモジュールをインポート 
import time
 
#RPi.GPIOモジュールをインポート 
import RPi.GPIO as GPIO
from pynput.keyboard import Key, Controller

# BCM(GPIO番号)で指定する設定 
GPIO.setmode(GPIO.BCM)
 
# GPIO17を出力モード設定 
GPIO.setup(17, GPIO.OUT)

keyboard = Controller()
try:
  while True:
      if keyboard.press(Key.space):
          GPIO.output(17, 1)
          time.sleep(0.5)
          GPIO.output(17, 0)
          time.sleep(0.5)
except KeyboardInterrupt:
  # GPIO設定クリア 
  GPIO.cleanup()
