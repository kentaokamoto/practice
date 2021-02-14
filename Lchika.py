#!/usr/bin/python 
# coding:utf-8 
 
from pynput.keyboard import Key, Controller

keyboard = Controller()
try:
  while True:
      if keyboard.press(Key.space):
except KeyboardInterrupt:
  
